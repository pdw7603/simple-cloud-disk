
<!-- src/views/Home.vue -->
<template>
  <div class="home-page" style="padding: 20px;">
    <div style="margin-bottom: 20px; display: flex; align-items: center; gap: 10px;">
      <h2>我的云盘</h2>
      <el-upload
        ref="uploadRef"
        :auto-upload="false"
        :on-change="handleFileChange"
        :show-file-list="false"
        action="#"
      >
        <el-button type="success">选择文件</el-button>
      </el-upload>
      <el-button type="primary" @click="handleUpload">上传文件</el-button>
    </div>

    <el-table :data="fileList" border style="width: 100%" v-loading="loading">
      <el-table-column prop="id" label="文件ID" width="180" />
      <el-table-column prop="file_name" label="文件名" min-width="200" />
      <el-table-column prop="file_size" label="文件大小(KB)" width="120" />
      <el-table-column prop="file_type" label="文件类型" width="120" />
      <el-table-column prop="upload_time" label="上传时间" width="180" />
      <el-table-column label="操作" width="180" fixed="right">
        <template #default="scope">
          <el-button size="small" @click="handleDownload(scope.row.id)">下载</el-button>
          <el-button size="small" type="danger" @click="handleDelete(scope.row.id)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { ElMessage, ElMessageBox } from 'element-plus'

// 请把下面的 IP 地址改成你自己的后端服务器 IP
const BASE_URL = 'http://192.168.142.128:9090'

const fileList = ref([])
const selectedFile = ref(null)
const uploadRef = ref(null)
const loading = ref(false)

// 页面加载时查询文件列表
onMounted(() => {
  getFileList()
})

// 1. 查询文件列表
const getFileList = async () => {
  loading.value = true
  try {
    const res = await axios.get(`${BASE_URL}/api/file/query?user_id=1`)
    if (res.data.code === 200) {
      fileList.value = res.data.data
    } else {
      ElMessage.error(res.data.msg)
    }
  } catch (err) {
    ElMessage.error('获取文件列表失败')
    console.error(err)
  } finally {
    loading.value = false
  }
}

// 2. 监听文件选择
const handleFileChange = (file) => {
  selectedFile.value = file
}

// 3. 上传文件
const handleUpload = async () => {
  if (!selectedFile.value) {
    return ElMessage.warning('请先选择文件！')
  }
  const formData = new FormData()
  formData.append('file', selectedFile.value.raw)
  formData.append('user_id', 1)
  try {
    const res = await axios.post(`${BASE_URL}/api/file/upload`, formData)
    if (res.data.code === 200) {
      ElMessage.success('上传成功！')
      uploadRef.value.clearFiles() // 清空选择的文件
      selectedFile.value = null
      getFileList() // 刷新列表
    } else {
      ElMessage.error(res.data.msg)
    }
  } catch (err) {
    ElMessage.error('文件上传失败')
    console.error(err)
  }
}

// 4. 下载文件
const handleDownload = async (fileId) => {
  try {
    const res = await axios.get(`${BASE_URL}/api/file/download?file_id=${fileId}&user_id=1`)
    if (res.data.code === 200) {
      // 创建下载链接
      const a = document.createElement('a')
      a.href = res.data.data.file_path
      a.download = res.data.data.file_name
      document.body.appendChild(a)
      a.click()
      document.body.removeChild(a)
      ElMessage.success('下载成功！')
    } else {
      ElMessage.error(res.data.msg)
    }
  } catch (err) {
    ElMessage.error('文件下载失败')
    console.error(err)
  }
}

// 5. 删除文件
const handleDelete = async (fileId) => {
  await ElMessageBox.confirm('确定要删除这个文件吗？', '提示', {
    type: 'warning'
  })
  try {
    const res = await axios.post(`${BASE_URL}/api/file/delete`, { file_id: fileId, user_id: 1 })
    if (res.data.code === 200) {
      ElMessage.success('删除成功！')
      getFileList() // 刷新列表
    } else {
      ElMessage.error(res.data.msg)
    }
  } catch (err) {
    ElMessage.error('文件删除失败')
    console.error(err)
  }
}
</script>

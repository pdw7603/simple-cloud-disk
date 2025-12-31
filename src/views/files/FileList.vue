<template>
  <div class="file-list-container">
    <div class="list-header">
      <h2>文件列表</h2>
      <el-button type="primary" @click="goToUpload">上传文件</el-button>
    </div>
    <el-table :data="fileList" border style="width: 100%;" v-loading="loading">
      <el-table-column prop="name" label="文件名" min-width="200" />
      <el-table-column prop="size" label="大小" width="120" />
      <el-table-column prop="updateTime" label="更新时间" width="180" />
      <el-table-column label="操作" width="180" align="center">
        <template #default="scope">
          <el-button type="text" size="small">下载</el-button>
          <el-button type="danger" size="small" @click="handleDelete(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage, ElMessageBox } from 'element-plus'
import { getFileList, deleteFile } from '../../api/file'

const router = useRouter()
const fileList = ref([])
const loading = ref(true)

const loadFiles = async () => {
  loading.value = true
  try {
    const response = await getFileList()
    fileList.value = response.data || []
  } catch (error) {
    console.error('加载文件列表失败:', error)
    fileList.value = []
  } finally {
    loading.value = false
  }
}

const goToUpload = () => router.push('/home/files/upload')

const handleDelete = async (row) => {
  try {
    await ElMessageBox.confirm('此操作将永久删除该文件, 是否继续?', '提示', {
      confirmButtonText: '确定',
      cancelButtonText: '取消',
      type: 'warning'
    })
    await deleteFile(row.id)
    ElMessage.success('删除成功')
    loadFiles()
  } catch (error) {
    if (error !== 'cancel') ElMessage.error('删除失败')
  }
}

onMounted(() => loadFiles())
</script>

<style scoped>
.file-list-container { padding: 20px; background: #fff; border-radius: 8px; box-shadow: 0 2px 12px rgba(0,0,0,0.1); }
.list-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
</style>

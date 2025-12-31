<template>
  <div class="file-upload-container">
    <h2>文件上传</h2>
    <el-upload
      class="upload-demo"
      :action="uploadUrl"
      :on-success="handleSuccess"
      :on-error="handleError"
      :before-upload="beforeUpload"
      list-type="picture-card"
    >
      <i class="el-icon-plus"></i>
    </el-upload>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'

const router = useRouter()
// 注意：这里的 action 路径需要与 vite.config.js 中的代理和后端接口匹配
// 我们的代理会将 /api/upload 转发到 http://localhost:9090/upload (或你的后端地址)
const uploadUrl = ref('/api/upload') 

const beforeUpload = (rawFile) => {
  // 这里可以添加文件大小和类型的校验
  if (rawFile.size / 1024 / 1024 > 10) {
    ElMessage.error('文件大小不能超过 10MB!')
    return false
  }
  return true
}

// 文件上传成功后的回调
const handleSuccess = (response, file) => {
  ElMessage.success(`文件 "${file.name}" 上传成功`)
  // 上传成功后，可以选择跳转到文件列表页
  // router.push('/home/files/list')
}

// 文件上传失败后的回调
const handleError = (err, file) => {
  ElMessage.error(`文件 "${file.name}" 上传失败`)
  console.error('上传失败:', err)
}
</script>

<style scoped>
.file-upload-container {
  padding: 20px;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.1);
}
.upload-demo {
  width: 100%;
}
</style>

<template>
  <div class="dashboard-container">
    <h2>仪表盘</h2>
    <p>欢迎使用云盘管理系统，这里是您的个人数据概览。</p>
    <el-row :gutter="20">
      <el-col :span="8">
        <div class="card">
          <h3>总文件数</h3>
          <p>1,234</p>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="card">
          <h3>已用空间</h3>
          <p>2.5 GB / 10 GB</p>
        </div>
      </el-col>
      <el-col :span="8">
        <div class="card">
          <h3>本月上传</h3>
          <p>320 个文件</p>
        </div>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'DashboardIndex' // 修复为多单词组件名
}
</script>

<style scoped>
.dashboard-container {
  padding: 20px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 12px rgba(0,0,0,0.1);
}
.card {
  background-color: #f9f9f9;
  padding: 20px;
  text-align: center;
  border-radius: 8px;
  h3 {
    margin: 0 0 10px 0;
    color: #666;
  }
  p {
    font-size: 24px;
    font-weight: bold;
    color: #1989fa;
    margin: 0;
  }
}
</style>

<template>
  <div class="home-container">
    <header class="main-header">
      <h1>云盘管理系统</h1>
      <div class="user-info">
        <!-- 动态显示用户名 -->
        <span>欢迎, {{ username }}</span>
        <el-button type="text" @click="logout">退出登录</el-button>
      </div>
    </header>
    <div class="main-body">
      <aside class="main-sidebar">
        <el-menu :default-active="$route.path" class="sidebar-menu" router>
          <el-menu-item index="/home">
            <i class="el-icon-s-home"></i>
            <template #title>首页</template>
          </el-menu-item>
          <el-submenu index="/home/files">
            <template #title>
              <i class="el-icon-folder-opened"></i>
              <span>文件管理</span>
            </template>
            <el-menu-item index="/home/files/list">文件列表</el-menu-item>
            <el-menu-item index="/home/files/upload">文件上传</el-menu-item>
          </el-submenu>
          <el-menu-item index="/home/profile">
            <i class="el-icon-user"></i>
            <template #title>个人中心</template>
          </el-menu-item>
        </el-menu>
      </aside>
      <main class="main-content">
        <router-view></router-view>
      </main>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      // 从localStorage获取用户名
      username: localStorage.getItem('username') || 'Guest'
    }
  },
  methods: {
    logout() {
      // 清除本地存储的token和用户名
      localStorage.removeItem('token');
      localStorage.removeItem('username');
      this.$router.push('/');
      this.$message.success('已成功退出登录');
    }
  }
}
</script>

<style lang="scss" scoped>
.home-container {
  display: flex;
  flex-direction: column;
  height: 100vh;
}
.main-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 60px;
  background-color: #1989fa;
  color: white;
  padding: 0 20px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  h1 { margin: 0; font-size: 20px; }
  .user-info {
    display: flex;
    align-items: center;
    gap: 20px;
    .el-button { color: white; }
  }
}
.main-body {
  display: flex;
  flex: 1;
  overflow: hidden;
}
.main-sidebar {
  width: 200px;
  background-color: #2f4050;
  color: white;
  .sidebar-menu:not(.el-menu--collapse) { width: 200px; }
  .el-menu { border-right: none; }
  .el-menu-item, .el-submenu__title { color: white; }
  .el-menu-item.is-active { background-color: #1989fa; }
}
.main-content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  background-color: #f3f3f4;
}
</style>

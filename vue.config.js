const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false, // 保留你原有的配置
  // 新增代理配置（对接后端8080端口）
  devServer: {
    port: 8083, // 前端启动端口
    proxy: {
      '/api/user': {
        target: 'http://localhost:8080', // 后端端口
        changeOrigin: true,
        pathRewrite: { '^/api/user': '/api/user' }
      }
    }
  }
})
module.exports = {
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:8080', // 后端服务地址
        changeOrigin: true, // 开启跨域
        pathRewrite: {
          '^/api': '' // 去掉请求路径中的/api前缀
        }
      }
    }
  }
};

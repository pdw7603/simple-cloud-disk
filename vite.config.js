import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5173,
    proxy: {
      // 代理所有以 /api 开头的请求到后端服务
      '/api': {
        target: 'http://localhost:9090', // 【重要】请将此处修改为您的后端API真实地址和端口
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }
})

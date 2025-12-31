<template>
  <div class="login-container">
    <el-card class="login-card">
      <div slot="header" class="login-header">
        <span>云盘管理系统</span>
      </div>
      <el-form :model="loginForm" :rules="loginRules" ref="loginFormRef" label-width="80px">
        <el-form-item label="用户名" prop="username">
          <el-input v-model="loginForm.username" placeholder="请输入用户名"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="loginForm.password" type="password" placeholder="请输入密码"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitLoginForm" :loading="loading">登录</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
// 假设登录API在 user.js 中，如果不在请调整
// 这里我们先创建一个模拟的登录函数，你需要替换成真实的API调用
// import { login } from '../api/user'

const router = useRouter()
const loading = ref(false)
const loginFormRef = ref(null)
const loginForm = ref({
  username: '',
  password: ''
})

const loginRules = ref({
  username: [{ required: true, message: '请输入用户名', trigger: 'blur' }],
  password: [{ required: true, message: '请输入密码', trigger: 'blur' }]
})

// 模拟登录API
const mockLogin = (data) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (data.username === 'admin' && data.password === '123456') {
        resolve({
          code: 200,
          message: '登录成功',
          data: {
            token: 'fake-token-for-testing',
            username: data.username
          }
        })
      } else {
        reject(new Error('用户名或密码错误'))
      }
    }, 1000)
  })
}

const submitLoginForm = async () => {
  if (!loginFormRef.value) return
  await loginFormRef.value.validate(async (valid) => {
    if (valid) {
      loading.value = true
      try {
        // 【重要】请将 mockLogin 替换为你真实的API调用
        // const response = await login(loginForm.value)
        const response = await mockLogin(loginForm.value)

        // 登录成功，保存token和用户名到localStorage
        localStorage.setItem('token', response.data.token)
        localStorage.setItem('username', response.data.username)

        ElMessage.success('登录成功！')
        // 跳转到首页
        router.push('/home')
      } catch (error) {
        console.error('登录失败:', error)
        ElMessage.error(error.message || '登录失败，请检查用户名和密码')
      } finally {
        loading.value = false
      }
    } else {
      console.log('登录表单校验失败')
      return false
    }
  })
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}
.login-card {
  width: 400px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.login-header {
  text-align: center;
  font-size: 20px;
  font-weight: bold;
}
</style>

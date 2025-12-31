<template>
  <div class="profile-container">
    <h2>个人中心</h2>

    <el-card shadow="never">
      <div class="profile-header">
        <el-avatar :size="100" icon="el-icon-user-solid"></el-avatar>
        <div class="user-info">
          <h3>{{ username }}</h3>
          <p>管理员</p>
        </div>
      </div>
    </el-card>

    <el-card shadow="never" style="margin-top: 20px;">
      <template #header>
        <span>修改密码</span>
      </template>
      <el-form :model="passwordForm" :rules="passwordRules" ref="passwordFormRef" label-width="120px">
        <el-form-item label="旧密码" prop="oldPassword">
          <el-input v-model="passwordForm.oldPassword" type="password" placeholder="请输入旧密码"></el-input>
        </el-form-item>
        <el-form-item label="新密码" prop="newPassword">
          <el-input v-model="passwordForm.newPassword" type="password" placeholder="请输入新密码"></el-input>
        </el-form-item>
        <el-form-item label="确认新密码" prop="confirmPassword">
          <el-input v-model="passwordForm.confirmPassword" type="password" placeholder="请再次输入新密码"></el-input>
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="submitPasswordForm">提交</el-button>
          <el-button @click="resetPasswordForm">重置</el-button>
        </el-form-item>
      </el-form>
    </el-card>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { ElMessage } from 'element-plus'
// 导入修改密码的API
import { updatePassword } from '../../api/user'

const router = useRouter()
// 从localStorage获取用户名，如果不存在则跳转到登录页
const username = ref(localStorage.getItem('username') || '')
if (!username.value) {
  router.push('/')
}

const passwordForm = ref({
  oldPassword: '',
  newPassword: '',
  confirmPassword: ''
})

const passwordFormRef = ref(null)

const passwordRules = ref({
  oldPassword: [{ required: true, message: '请输入旧密码', trigger: 'blur' }],
  newPassword: [{ required: true, message: '请输入新密码', trigger: 'blur' }, { min: 6, message: '密码长度不能少于6位', trigger: 'blur' }],
  confirmPassword: [{ required: true, message: '请确认新密码', trigger: 'blur' },
    {
      validator: (rule, value, callback) => {
        if (value !== passwordForm.value.newPassword) {
          callback(new Error('两次输入的密码不一致'))
        } else {
          callback()
        }
      },
      trigger: 'blur'
    }
  ]
})

const submitPasswordForm = async () => {
  if (!passwordFormRef.value) return
  await passwordFormRef.value.validate(async (valid) => {
    if (valid) {
      try {
        // 调用修改密码API
        await updatePassword({
          oldPassword: passwordForm.value.oldPassword,
          newPassword: passwordForm.value.newPassword
        })
        ElMessage.success('密码修改成功！请重新登录。')
        // 修改成功后，清除本地存储并跳转到登录页
        localStorage.removeItem('token')
        localStorage.removeItem('username')
        router.push('/')
      } catch (error) {
        console.error('修改密码失败:', error)
        // 错误信息会由 request.js 的响应拦截器处理
      }
    } else {
      ElMessage.error('请检查表单信息！')
    }
  })
}

const resetPasswordForm = () => {
  if (!passwordFormRef.value) return
  passwordFormRef.value.resetFields()
}
</script>

<style scoped>
.profile-container { padding: 20px; }
.profile-header { display: flex; align-items: center; gap: 20px; padding: 20px; }
.user-info h3 { margin: 0 0 5px 0; }
.user-info p { margin: 0; color: #999; }
</style>

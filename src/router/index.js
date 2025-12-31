import { createRouter, createWebHistory } from 'vue-router'
import { ElMessage } from 'element-plus'

// 页面组件（使用懒加载）
const Login = () => import('@/views/Login.vue')
const HomePage = () => import('@/views/HomePage.vue')
const FileList = () => import('@/views/files/FileList.vue')
const FileUpload = () => import('@/views/files/FileUpload.vue')
const ProfilePage = () => import('@/views/profile/ProfilePage.vue')

// 错误页面
const NotFound = () => import('@/views/error/NotFound.vue')
const NoPermission = () => import('@/views/error/NoPermission.vue')

const routes = [
  {
    path: '/',
    redirect: '/login'
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
    meta: {
      title: '登录 - 云盘管理系统',
      requiresAuth: false
    }
  },
  {
    path: '/home',
    name: 'Home',
    component: HomePage,
    meta: {
      title: '首页 - 云盘管理系统',
      requiresAuth: true
    },
    children: [
      {
        path: '',
        redirect: '/home/dashboard'
      },
      {
        path: 'dashboard',
        name: 'Dashboard',
        component: FileList, // 首页显示文件列表
        meta: {
          title: '首页',
          icon: 'el-icon-s-home',
          requiresAuth: true
        }
      },
      {
        path: 'files',
        name: 'Files',
        redirect: '/home/files/list',
        meta: {
          title: '文件管理',
          icon: 'el-icon-folder-opened',
          requiresAuth: true
        },
        children: [
          {
            path: 'list',
            name: 'FileList',
            component: FileList,
            meta: {
              title: '文件列表',
              icon: 'el-icon-document',
              requiresAuth: true
            }
          },
          {
            path: 'upload',
            name: 'FileUpload',
            component: FileUpload,
            meta: {
              title: '文件上传',
              icon: 'el-icon-upload2',
              requiresAuth: true
            }
          }
        ]
      },
      {
        path: 'profile',
        name: 'Profile',
        component: ProfilePage,
        meta: {
          title: '个人中心',
          icon: 'el-icon-user',
          requiresAuth: true
        }
      }
    ]
  },
  // 错误页面
  {
    path: '/404',
    name: 'NotFound',
    component: NotFound,
    meta: {
      title: '页面不存在',
      requiresAuth: false
    }
  },
  {
    path: '/403',
    name: 'NoPermission',
    component: NoPermission,
    meta: {
      title: '无权限访问',
      requiresAuth: false
    }
  },
  // 404通配路由
  {
    path: '/:pathMatch(.*)*',
    redirect: '/404'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

// 路由守卫
router.beforeEach((to, from, next) => {
  // 设置页面标题
  const title = to.meta.title || '云盘管理系统'
  document.title = title
  
  // 检查是否需要认证
  if (to.meta.requiresAuth) {
    const token = localStorage.getItem('token')
    
    if (!token) {
      ElMessage.warning('请先登录')
      next('/login')
      return
    }
    
    // 验证token有效性（这里可以添加更复杂的验证逻辑）
    if (token === 'demo-token-123456') {
      // 演示模式token，直接通过
      next()
    } else {
      // 实际验证逻辑
      try {
        // 这里可以添加JWT验证逻辑
        const tokenData = JSON.parse(atob(token.split('.')[1]))
        const now = Math.floor(Date.now() / 1000)
        
        if (tokenData.exp && tokenData.exp < now) {
          ElMessage.warning('登录已过期，请重新登录')
          localStorage.removeItem('token')
          localStorage.removeItem('username')
          next('/login')
          return
        }
        
        next()
      } catch (error) {
        console.error('Token验证失败:', error)
        ElMessage.warning('登录状态异常，请重新登录')
        localStorage.removeItem('token')
        localStorage.removeItem('username')
        next('/login')
      }
    }
  } else {
    // 不需要认证的页面
    if (to.path === '/login') {
      const token = localStorage.getItem('token')
      if (token) {
        // 如果已登录，跳转到首页
        next('/home')
        return
      }
    }
    next()
  }
})

// 路由错误处理
router.onError((error) => {
  console.error('路由错误:', error)
  
  // 如果是组件加载失败，提示用户刷新
  if (error.message.includes('Failed to fetch dynamically imported module')) {
    ElMessage.error('页面加载失败，请刷新重试')
  }
})

export default router

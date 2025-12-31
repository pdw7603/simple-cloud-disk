// API配置（成员C开发 - 用于后端联调）
// ==============================================
// ★★★ 老师注意：这里配置后端服务地址 ★★★
// 如果老师要修改后端地址，只需修改下面的BASE_URL
// ==============================================

// 后端服务基础地址（根据老师的后端服务调整）
export const BASE_URL = 'http://localhost:9090'  // A模块（用户认证）
export const FILE_SERVICE_URL = 'http://localhost'  // B模块（文件操作）

// API路径映射
export const API_PATHS = {
  // 用户认证相关（A模块）
  USER: {
    LOGIN: '/api/user/login',
    LOGOUT: '/api/user/logout',
    INFO: '/api/user/info',
    UPDATE_PASSWORD: '/api/user/updatePassword',
    UPDATE_PROFILE: '/api/user/updateProfile'
  },
  
  // 文件操作相关（B模块）
  FILE: {
    UPLOAD: '/api/file/upload',
    LIST: '/api/file/list',
    QUERY: '/api/file/query',
    DELETE: '/api/file/delete',
    DOWNLOAD: '/api/file/download',
    BATCH_DELETE: '/api/file/batchDelete',
    SEARCH: '/api/file/search'
  },
  
  // 系统状态
  SYSTEM: {
    HEALTH: '/api/system/health',
    STATS: '/api/system/stats'
  }
}

// 文件类型映射（用于前端显示）
export const FILE_TYPES = {
  document: { label: '文档', icon: 'Document', color: '#409EFF', tagType: 'primary' },
  image: { label: '图片', icon: 'Picture', color: '#67C23A', tagType: 'success' },
  video: { label: '视频', icon: 'VideoPlay', color: '#E6A23C', tagType: 'warning' },
  audio: { label: '音频', icon: 'Headset', color: '#E6A23C', tagType: 'warning' },
  archive: { label: '压缩包', icon: 'Files', color: '#F56C6C', tagType: 'danger' },
  pdf: { label: 'PDF', icon: 'Document', color: '#409EFF', tagType: 'primary' },
  other: { label: '其他', icon: 'Files', color: '#909399', tagType: 'info' }
}

// 上传配置
export const UPLOAD_CONFIG = {
  MAX_SIZE: 100 * 1024 * 1024, // 100MB
  ACCEPT_TYPES: '.jpg,.jpeg,.png,.gif,.pdf,.doc,.docx,.xls,.xlsx,.ppt,.pptx,.zip,.rar,.txt',
  CHUNK_SIZE: 5 * 1024 * 1024, // 5MB分片
  MAX_FILES: 10 // 同时上传最大文件数
}

// 分页配置
export const PAGINATION_CONFIG = {
  DEFAULT_PAGE_SIZE: 10,
  PAGE_SIZES: [10, 20, 50, 100]
}

// 错误码映射（前端显示友好提示）
export const ERROR_CODES = {
  200: '操作成功',
  400: '请求参数错误',
  401: '未授权，请重新登录',
  403: '权限不足',
  404: '资源不存在',
  500: '服务器内部错误',
  1001: '用户名或密码错误',
  1002: 'Token已过期',
  1003: '文件上传失败',
  1004: '文件不存在',
  1005: '文件删除失败',
  1006: '文件大小超过限制',
  1007: '文件格式不支持'
}

// 模拟数据开关（开发/演示模式）
export const IS_DEMO_MODE = true // 设置为false时禁用模拟数据

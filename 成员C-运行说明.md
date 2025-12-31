# 成员C-前端交互模块 老师运行指南（100%成功）

## 一、运行位置
任意系统终端（Linux/Windows/macOS），请使用一个全新的、独立的终端窗口。

## 二、运行前置要求
1. 安装 Node.js (v18+)：https://nodejs.org/zh-cn/download/
2. 验证安装：`node -v` 和 `npm -v` 能显示版本号。

## 三、完整运行步骤（复制即执行）
1. 进入模块目录：
    cd 桌面/03_前端交互模块-成员C
2. 安装依赖：
    npm install --registry=https://registry.npmmirror.com
3. 启动服务：
    npm run dev
4. 访问页面：
    浏览器打开 http://localhost:5173

## 四、成功标识
✅ 终端显示 `VITE v... ready in ... ms`。
✅ 浏览器打开 `http://localhost:5173` 能看到登录页。

## 五、停止命令
在启动服务的终端中，按 `Ctrl + C`，然后按 `Enter`。

## 六、常见问题解决
1. 依赖安装失败：重试 `npm install` 命令。
2. 页面空白：确保 `npm install` 成功，然后重启服务 (`Ctrl + C` 再 `npm run dev`)。
3. 登录/按钮无反应：**此问题与前端无关**，是成员A或B的后端服务未启动或配置错误。

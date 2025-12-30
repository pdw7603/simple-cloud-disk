# 文件模块 BUG 修复记录
## 一、 修复基本信息
-  修复时间：2025-12-30
-  模块名称：文件操作模块（upload/query/download/delete）
-  修复人员：root
-  服务器环境：hadoop1（Linux + MariaDB 5.5 + Python3.6）

## 二、 待修复问题清单
1.  文件上传报错：返回 code=500，提示「文件不能为空」
2.  数据库操作报错：返回 code=500，提示「Access denied for user 'root'@'localhost' (using password: NO)」
3.  文件下载报错：返回 code=500，提示「服务器上的物理文件不存在」
4.  数据库 1054 报错：未知列 file_type、is_delete、update_time
5.  脚本路径错误：提示「没有那个文件或目录」
6.  sed 命令解析报错：提示「“s”的未知选项」

## 三、 针对性修复方案
### 1.  文件不能为空（上传报错）
-  问题根源：脚本测试文件路径配置错误，指向不存在的 /test_download.txt
-  修复方案：用 sed 命令修改为真实测试文件路径（改用 # 作为分隔符规避 / 冲突），并在脚本目录创建 test_file.txt
-  修复结果：上传功能正常，返回 code=200

### 2.  数据库连接失败（Access denied）
-  问题根源：脚本 DB_CONFIG 字典中 password 为空，未配置 MySQL 密码 123456
-  修复方案：批量修改 4 个核心脚本，将 password 改为 '123456'
-  修复结果：数据库连接正常，查询/删除操作可正常访问数据库

### 3.  物理文件不存在（下载报错）
-  问题根源：/opt/cloud-disk/ 目录下无对应测试文件
-  修复方案：创建 /opt/cloud-disk/upload /opt/cloud-disk/download 目录，复制 test_file.txt 至对应目录
-  修复结果：下载功能正常，返回 code=200

### 4.  数据库 1054 未知列报错
-  问题根源：file_info、file_metadata 表缺失 file_type、is_delete、update_time 字段，与脚本 SQL 不匹配
-  修复方案：交互式登录 MariaDB，给对应表新增缺失字段，适配脚本需求
-  修复结果：1054 报错消除，数据库操作正常

### 5.  脚本路径错误
-  问题根源：目录 /root/simple-cloud-disk/backend/file-hadoop 不存在，或路径输入错误
-  修复方案：用 mkdir -p 递归创建目录，用 find 命令定位真实脚本路径
-  修复结果：可正常进入脚本目录，执行脚本无路径报错

### 6.  sed 命令解析报错
-  问题根源：sed 替换指令中 / 与路径分隔符 / 冲突
-  修复方案：改用 # 作为 sed 替换分隔符，规避解析冲突
-  修复结果：sed 命令执行成功，脚本路径修改生效

## 四、 修复最终结果
1.  核心功能：4 大功能（上传/查询/下载/删除）均返回 code=200，无报错，100% 可用
2.  交付物：已创建接口文档、运行说明、BUG 修复记录 3 个 .md 文件
3.  代码状态：所有修改已提交并推送至 GitHub file-hadoop-module 分支
4.  环境状态：服务器环境、数据库配置、目录文件均已就绪，可直接部署使用

## 五、 备注
-  若后续修改数据库密码，需同步更新 4 个脚本的 DB_CONFIG 字典
-  新增文件类型时，无需修改脚本，自动记录 file_type 字段
-  该模块为逻辑删除，文件标记为 is_delete=1 后，不再显示在查询结果中

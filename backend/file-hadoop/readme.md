# 文件操作模块运行说明
## 一、 运行环境要求
1.  操作系统：Linux（CentOS 7+/Ubuntu 16.04+）
2.  Python 版本：3.6 及以上
3.  数据库版本：MariaDB 5.5+ / MySQL 5.7+
4.  依赖库：pymysql（执行 pip3 install pymysql 安装）

## 二、 前置准备工作
1.  数据库配置：
    -  已创建 cloud_disk 数据库
    -  已创建 file_info 和 file_metadata 表，并补充完整字段（file_type、is_delete、create_time、update_time）
    -  数据库用户 root 密码为 123456（可在 DB_CONFIG 字典中修改）
2.  目录创建：
    -  服务器需创建 /opt/cloud-disk/ 及子目录（upload、download）
    -  执行命令：mkdir -p /opt/cloud-disk/upload /opt/cloud-disk/download && chmod -R 777 /opt/cloud-disk
3.  脚本配置：
    -  4 个核心脚本（upload_file.py、query_file.py、download_file.py、delete_file.py）已补充数据库密码
    -  测试文件 test_file.txt 已放置在脚本目录，并同步至 /opt/cloud-disk/ 目录

## 三、 运行方式
1.  进入脚本目录：cd /root/simple-cloud-disk/backend/file-hadoop
2.  单独运行某个功能：
    -  上传文件：python3 upload_file.py
    -  查询文件：python3 query_file.py
    -  下载文件：python3 download_file.py
    -  删除文件：python3 delete_file.py
3.  一键运行所有功能测试：执行批量测试命令（详见测试文档）

## 四、 常见问题排查
1.  Access denied 报错：检查脚本中 DB_CONFIG 字典的密码是否正确（默认 123456）
2.  Unknown column 报错：检查数据库表是否缺失对应字段（如 file_type、is_delete、update_time）
3.  物理文件不存在：检查 /opt/cloud-disk/ 目录下是否存在对应文件，同步测试文件即可
4.  权限不足：执行 chmod -R 777 /opt/cloud-disk 赋予目录读写权限

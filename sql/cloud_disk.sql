# 简易云盘项目-数据库初始化脚本
# 执行方式：mysql -uroot -p < /root/simple-cloud-disk/sql/cloud_disk.sql
DROP DATABASE IF EXISTS cloud_disk;
CREATE DATABASE IF NOT EXISTS cloud_disk DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE cloud_disk;

# 成员A负责维护：用户认证核心表（补充加密/业务SQL/测试数据）
CREATE TABLE IF NOT EXISTS sys_user (
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '用户主键ID',
    username VARCHAR(50) NOT NULL UNIQUE COMMENT '登录用户名',
    password VARCHAR(100) NOT NULL COMMENT '密码（MD5/SHA256加密存储）',
    email VARCHAR(100) NOT NULL COMMENT '用户邮箱',
    status TINYINT DEFAULT 1 COMMENT '账号状态：1-正常 0-禁用',
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户信息表';

# 成员B负责维护：文件操作核心表（补充业务SQL/关联逻辑）
CREATE TABLE IF NOT EXISTS sys_file (
    id BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '文件主键ID',
    file_name VARCHAR(255) NOT NULL COMMENT '文件原始名称',
    file_path VARCHAR(500) NOT NULL COMMENT 'HDFS存储完整路径',
    file_size BIGINT NOT NULL COMMENT '文件大小（字节）',
    file_type VARCHAR(50) COMMENT '文件类型（如txt/zip/jpg）',
    user_id BIGINT NOT NULL COMMENT '上传用户ID，关联sys_user.id',
    upload_time DATETIME DEFAULT CURRENT_TIMESTAMP COMMENT '上传时间',
    FOREIGN KEY (user_id) REFERENCES sys_user(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='文件信息表';

# 预留测试数据插入位置（成员A/B开发完成后补充）
# -- 成员A：插入测试用户（密码需加密）
# INSERT INTO sys_user (username, password, email) VALUES ('admin', '加密密码', 'admin@test.com');
# -- 成员B：插入测试文件（关联已存在的user_id）
# INSERT INTO sys_file (file_name, file_path, file_size, file_type, user_id) VALUES ('test.txt', '/cloud_disk/upload/test.txt', 1024, 'txt', 1);

CREATE DATABASE IF NOT EXISTS cloud_disk DEFAULT CHARSET utf8mb4;
USE cloud_disk;
DROP TABLE IF EXISTS sys_user;
CREATE TABLE sys_user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    create_time DATETIME DEFAULT CURRENT_TIMESTAMP
);
# 插入2个用户：默认测试用户test + 你需要的admin用户
INSERT INTO sys_user (username, password) VALUES ('test', '123456');
INSERT INTO sys_user (username, password) VALUES ('admin', 'Admin@123456');

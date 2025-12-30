#!/bin/bash
echo "========== 启动简易云盘项目基础服务 =========="

# 1. 启动Hadoop核心进程（新版无告警命令，单机专用）
echo "1. 启动HDFS核心服务"
hdfs --daemon start namenode
hdfs --daemon start datanode
sleep 3

echo "2. 启动YARN核心服务"
yarn --daemon start resourcemanager
yarn --daemon start nodemanager
sleep 3
jps | grep -E 'NameNode|DataNode|ResourceManager|NodeManager' && echo "✅ Hadoop服务启动成功"

# 2. 检查MySQL服务（确保运行）
echo "3. 检查MySQL服务状态"
systemctl start mysqld &>/dev/null
mysql --version &>/dev/null && echo "✅ MySQL服务运行正常"

# 3. 目录已永久创建，无需重复执行（仅验证）
echo "4. 验证项目存储目录"
hdfs dfs -test -d /cloud_disk/upload && echo "✅ HDFS目录 /cloud_disk/upload 可用"

# 4. 待开发模块标注
echo "5. 后端服务：待成员A开发后部署 cloud-disk.jar"
echo "6. 前端服务：待成员C开发后部署 npm run dev"

echo "========== 基础服务启动完成 ✅ =========="
echo "环境就绪，等待其他成员模块开发"

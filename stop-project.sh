#!/bin/bash
echo "开始停止简易云盘项目所有服务..."

# 1. 停止Hadoop单机服务（精准停止核心进程，适配无slave环境）
echo "第一步：停止Hadoop单机集群服务"
hadoop-daemon.sh stop namenode
hadoop-daemon.sh stop datanode
yarn-daemon.sh stop resourcemanager
yarn-daemon.sh stop nodemanager
echo "Hadoop单机集群服务已停止"

# 2. 停止MySQL服务（按需启停，可选）
echo "第二步：停止MySQL服务"
systemctl stop mysqld
echo "MySQL服务已停止"

# 3. 跳过前后端停止（待开发完成后补充）
echo "第三步：后端服务-待开发完成后执行 kill -9 进程号"
echo "第四步：前端服务-待开发完成后执行 kill -9 进程号"

echo "简易云盘项目所有服务停止完成！"

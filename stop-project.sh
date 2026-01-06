#!/bin/bash
echo "========== 停止简易云盘项目基础服务 =========="

# 1. 精准停止Hadoop所有进程（无冗余报错）
echo "1. 停止HDFS服务"
hdfs --daemon stop namenode
hdfs --daemon stop datanode

echo "2. 停止YARN服务"
yarn --daemon stop resourcemanager
yarn --daemon stop nodemanager
echo "✅ Hadoop服务已全部停止"

# 2. 停止MySQL服务
echo "3. 停止MySQL服务"
systemctl stop mysqld &>/dev/null
echo "✅ MySQL服务已停止"

# 3. 待开发模块标注
echo "4. 后端服务：开发完成后执行 kill -9 进程号"
echo "5. 前端服务：开发完成后执行 kill -9 进程号"

echo "========== 所有服务停止完成 ✅ =========="

#!/bin/bash
# 成员D编写：项目一键停止脚本（顺序：前端→后端→Hadoop）
echo "开始停止简易云盘项目所有服务..."

# 1. 停止前端服务
echo "第一步：停止前端服务"
ps -ef | grep npm | grep -v grep | awk '{print $2}' | xargs kill -9 &>/dev/null
echo "前端服务已停止"

# 2. 停止后端服务
echo "第二步：停止后端服务"
ps -ef | grep cloud-disk.jar | grep -v grep | awk '{print $2}' | xargs kill -9 &>/dev/null
echo "后端服务已停止"

# 3. 停止Hadoop集群
echo "第三步：停止Hadoop集群"
stop-all.sh &>/dev/null
echo "Hadoop集群已停止"

echo "简易云盘项目所有服务停止完成！"

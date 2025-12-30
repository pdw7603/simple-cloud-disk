#!/bin/bash
# 成员D编写：项目一键启动脚本（顺序：Hadoop→数据库→后端→前端）
echo "开始启动简易云盘项目所有服务..."

# 1. 启动Hadoop集群
echo "第一步：启动Hadoop集群"
start-all.sh
sleep 5
jps | grep -E 'NameNode|DataNode|ResourceManager|NodeManager' && echo "Hadoop集群启动成功" || echo "Hadoop集群启动异常"

# 2. 检查MySQL服务状态，未启动则启动
echo "第二步：检查并启动MySQL服务"
systemctl status mysqld &>/dev/null || systemctl start mysqld
mysql --version &>/dev/null && echo "MySQL服务运行正常" || echo "MySQL服务启动失败"

# 3. 启动后端服务（后台运行，不占用终端）
echo "第三步：启动后端服务"
cd /home/root/simple-cloud-disk/backend
nohup java -jar cloud-disk.jar > backend.log 2>&1 &
sleep 3
ps -ef | grep cloud-disk.jar | grep -v grep && echo "后端服务启动成功" || echo "后端服务启动失败"

# 4. 启动前端服务（后台运行）
echo "第四步：启动前端服务"
cd /home/root/simple-cloud-disk/frontend
nohup npm run dev > frontend.log 2>&1 &
sleep 3
ps -ef | grep npm | grep -v grep && echo "前端服务启动成功" || echo "前端服务启动失败"

echo "简易云盘项目所有服务启动完成！"
echo "前端访问地址：http://虚拟机IP:8080 后端接口地址：http://虚拟机IP:9090"

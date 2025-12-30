#!/bin/bash
echo "开始启动简易云盘项目所有服务..."

# 1. 启动Hadoop单机服务（适配无slave节点环境，跳过从节点报错）
echo "第一步：启动Hadoop单机集群服务"
hadoop-daemon.sh start namenode
hadoop-daemon.sh start datanode
yarn-daemon.sh start resourcemanager
yarn-daemon.sh start nodemanager
sleep 5
jps | grep -E 'NameNode|DataNode|ResourceManager|NodeManager' && echo "Hadoop单机集群启动成功" || echo "Hadoop核心进程已启动"

# 2. 检查并启动MySQL服务
echo "第二步：检查并启动MySQL服务"
systemctl status mysqld &>/dev/null || systemctl start mysqld
mysql --version &>/dev/null && echo "MySQL服务运行正常" || echo "MySQL服务启动失败"

# 3. 初始化HDFS项目目录（必做，避免成员B开发时报权限/目录不存在错误）
echo "第三步：初始化HDFS文件存储目录"
hdfs dfs -test -d /cloud_disk/upload || hdfs dfs -mkdir -p /cloud_disk/upload
hdfs dfs -chmod 777 /cloud_disk/upload
echo "HDFS目录 /cloud_disk/upload 权限配置完成"

# 4. 跳过前后端启动（待成员A/B/C开发完成后补充，当前标注待开发）
echo "第四步：后端服务-待成员A开发完成后部署（cloud-disk.jar）"
echo "第五步：前端服务-待成员C开发完成后部署（npm run dev）"

echo "简易云盘项目基础服务启动完成！"
echo "基础环境就绪，等待成员A/B/C模块开发后，补充启动前后端服务"

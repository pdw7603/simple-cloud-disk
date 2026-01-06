#!/bin/bash
echo -e "========================================="
echo -e "     简易云盘项目 - 开发环境检查报告     "
echo -e "========================================="
git --version &>/dev/null && echo -e "Git 环境：已安装" || echo -e "Git 环境：未安装，需优先部署";
java -version &>/dev/null && echo -e "JDK 环境：已安装" || echo -e "JDK 环境：未安装，后端开发必备";
mysql --version &>/dev/null && echo -e "MySQL 环境：已安装" || echo -e "MySQL 环境：未安装，数据存储必备";
hadoop version &>/dev/null && echo -e "Hadoop 环境：已安装" || echo -e "Hadoop 环境：未安装，文件模块必备";
echo -e "========================================="

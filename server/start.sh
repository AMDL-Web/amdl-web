#!/bin/bash

# Apple Music Link Parser 后端启动脚本

echo "正在启动 Apple Music Link Parser 后端服务..."

# 检查 Python 环境
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到 Python3，请先安装 Python3"
    exit 1
fi

# 安装依赖
echo "正在安装依赖..."
pip3 install -r requirements.txt

# 启动服务
echo "正在启动服务..."
cd python
python3 backend.py

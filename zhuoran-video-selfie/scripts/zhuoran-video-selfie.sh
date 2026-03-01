#!/bin/bash
#
# 卓然视频自拍技能 - Bash 包装脚本（OpenClaw 入口）
# 用法: ./zhuoran-video-selfie.sh <scene> [options]
#

set -e

# 获取脚本目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE="${OPENCLAW_WORKSPACE:-/Users/delta/.openclaw/workspace}"

# Python 脚本路径
PYTHON_SCRIPT="${SCRIPT_DIR}/zhuoran-video-selfie.py"

# 检查 Python 脚本是否存在
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "[错误] 未找到 Python 脚本: $PYTHON_SCRIPT" >&2
    exit 1
fi

# 执行 Python 脚本
python3 "$PYTHON_SCRIPT" "$@"

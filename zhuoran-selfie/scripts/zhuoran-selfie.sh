#!/bin/bash
# zhuoran-selfie.sh - OpenClaw 兼容入口脚本
#
# 用法:
#   ./zhuoran-selfie.sh <scene> [options]
#
# 环境变量:
#   WAVESPEED_KEY - WaveSpeed AI API key (可选，脚本有默认值)
#
# 示例:
#   ./zhuoran-selfie.sh office
#   ./zhuoran-selfie.sh cafe --mode selfie
#   ./zhuoran-selfie.sh gym --target "@username" --caption "健身打卡"

set -euo pipefail

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(cd "${SCRIPT_DIR}/../.." && pwd)"

# 检查 Python
if ! command -v python3 &> /dev/null; then
    log_error "python3 未安装"
    exit 1
fi

# 解析参数
if [ $# -lt 1 ]; then
    echo "用法: $0 <scene> [options]"
    echo ""
    echo "场景:"
    echo "  office, cafe, airport, westlake, bookstore, gym, beach, selfie_late_night"
    echo ""
    echo "选项:"
    echo "  --mode <direct|selfie|portrait>   生成模式 (默认: direct)"
    echo "  --method <one_step|two_step|smart> 生成方法 (默认: smart)"
    echo "  --target <@user|#channel>         发送目标（可选）"
    echo "  --caption <text>                  配文（可选）"
    echo "  --output <path>                   输出路径（可选）"
    echo ""
    echo "示例:"
    echo "  $0 office"
    echo "  $0 cafe --mode selfie"
    echo "  $0 gym --target '@username' --caption '健身打卡'"
    exit 1
fi

SCENE="$1"
shift
# 剩余参数传递给 Python 脚本

# 调用 Python 脚本
log_info "启动卓然自拍技能..."
log_info "场景: $SCENE"

python3 "${SCRIPT_DIR}/zhuoran-selfie.py" "$SCENE" "$@"

EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    log_info "技能执行完成"
else
    log_error "技能执行失败 (退出码: $EXIT_CODE)"
    exit $EXIT_CODE
fi

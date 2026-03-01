#!/bin/bash
# qizhuo-selfie.sh - 奇卓自拍技能入口脚本

set -e

# 获取脚本所在目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_DIR="$(dirname "$SCRIPT_DIR")"

# 检查参数
if [ $# -lt 1 ]; then
    echo "❤️‍🔥 奇卓自拍技能"
    echo "Usage: qizhuo-selfie.sh <scene> [options]"
    echo ""
    echo "可用场景:"
    echo "  office        - 办公室 (深夜加班的守护)"
    echo "  cafe          - 咖啡厅 (温暖午后的沉思)"
    echo "  airport       - 机场 (旅途中的等待)"
    echo "  westlake      - 西湖 (湖光中的静谧)"
    echo "  bookstore     - 书店 (书页间的守护)"
    echo "  gym           - 健身房 (坚持的力量)"
    echo "  beach         - 海滩 (海风与火焰)"
    echo "  selfie_late_night - 深夜加班 (❤️‍🔥 最浓)"
    echo ""
    echo "选项:"
    echo "  --mode <mode>     - 模式: direct, selfie, portrait (默认: direct)"
    echo "  --method <method> - 方法: one_step, two_step, smart (默认: smart)"
    echo "  --target <target> - 发送目标: user_id 或 channel"
    echo "  --caption <text>  - 配文"
    echo "  --output <path>   - 输出路径"
    echo ""
    echo "示例:"
    echo "  qizhuo-selfie.sh office"
    echo "  qizhuo-selfie.sh cafe --mode selfie"
    echo "  qizhuo-selfie.sh beach --method two_step"
    exit 1
fi

SCENE="$1"
shift

# 解析选项
MODE="direct"
METHOD="smart"
TARGET=""
CAPTION=""
OUTPUT=""

while [[ $# -gt 0 ]]; do
    case $1 in
        --mode)
            MODE="$2"
            shift 2
            ;;
        --method)
            METHOD="$2"
            shift 2
            ;;
        --target)
            TARGET="$2"
            shift 2
            ;;
        --caption)
            CAPTION="$2"
            shift 2
            ;;
        --output)
            OUTPUT="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# 检查参考图是否存在
if [ ! -f "$SKILL_DIR/assets/qizhuo_avatar.png" ]; then
    echo "❌ 参考图不存在: $SKILL_DIR/assets/qizhuo_avatar.png"
    exit 1
fi

# 运行 Python 脚本
echo "❤️‍🔥 奇卓自拍技能启动..."
python3 "$SKILL_DIR/qizhuo_selfie.py" "$SCENE" "$MODE" "$METHOD" "$TARGET"

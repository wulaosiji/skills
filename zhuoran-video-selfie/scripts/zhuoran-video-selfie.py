#!/usr/bin/env python3
"""
卓然视频自拍技能 - Python CLI 入口
支持生成视频并发送到飞书
"""

import os
import sys
import argparse

# 添加技能目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/..')

from zhuoran_video_selfie import generate_video, DISABLED_SCENES, SCENE_TEMPLATES

def send_video_to_feishu(video_path, target_id, caption=None):
    """
    发送视频到飞书
    
    Args:
        video_path: 视频文件路径
        target_id: 目标用户/群ID
        caption: 配文（可选）
    
    Returns:
        是否发送成功
    """
    try:
        # 尝试使用 feishu-video-sender 技能
        sender_path = os.path.expanduser(
            "~/.openclaw/workspace/skills/feishu-video-sender/feishu_video_sender.py"
        )
        
        if not os.path.exists(sender_path):
            print(f"[错误] 未找到飞书视频发送工具: {sender_path}", file=sys.stderr)
            return False
        
        import subprocess
        cmd = ["python3", sender_path, video_path, target_id]
        
        if caption:
            cmd.extend(["--caption", caption])
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"[成功] 视频已发送到: {target_id}", file=sys.stderr)
            return True
        else:
            print(f"[错误] 发送失败: {result.stderr}", file=sys.stderr)
            return False
            
    except Exception as e:
        print(f"[错误] 发送视频时出错: {e}", file=sys.stderr)
        return False

def main():
    parser = argparse.ArgumentParser(
        description='卓然视频自拍技能 - 生成场景化自拍视频',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
可用场景:
  office     - 办公室场景
  cafe       - 咖啡厅场景  
  westlake   - 西湖场景
  gym        - 健身房场景

示例:
  # 生成办公室自拍视频
  python3 zhuoran-video-selfie.py office
  
  # 生成并发送到指定用户
  python3 zhuoran-video-selfie.py cafe --target ou_xxx
  
  # 生成3秒短视频
  python3 zhuoran-video-selfie.py gym --duration 3
        """
    )
    
    parser.add_argument(
        'scene',
        choices=list(SCENE_TEMPLATES.keys()),
        help='场景代码'
    )
    
    parser.add_argument(
        '--duration',
        type=int,
        default=5,
        choices=[3, 5, 10],
        help='视频时长（秒，默认5秒，建议不超过5秒）'
    )
    
    parser.add_argument(
        '--target',
        type=str,
        help='目标用户/群ID（发送视频）'
    )
    
    parser.add_argument(
        '--caption',
        type=str,
        default=None,
        help='视频配文'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        help='输出路径（默认 /tmp/zhuoran_{scene}_video.mp4）'
    )
    
    parser.add_argument(
        '--list-scenes',
        action='store_true',
        help='列出所有可用场景'
    )
    
    args = parser.parse_args()
    
    # 列出场景
    if args.list_scenes:
        print("可用场景:")
        for scene, info in SCENE_TEMPLATES.items():
            print(f"  {scene:12} - {info['change_level']}变化")
        return 0
    
    # 检查禁用场景
    if args.scene in DISABLED_SCENES:
        print(f"[错误] 场景 '{args.scene}' 已被禁用（高风险场景，避免使用）", file=sys.stderr)
        return 1
    
    try:
        # 生成视频
        print(f"[信息] 开始生成 '{args.scene}' 场景视频，时长 {args.duration} 秒...", file=sys.stderr)
        
        video_path = generate_video(
            scene=args.scene,
            duration=args.duration,
            output_path=args.output
        )
        
        print(f"[成功] 视频已生成: {video_path}")
        
        # 发送到飞书（如果指定了target）
        if args.target:
            send_video_to_feishu(video_path, args.target, args.caption)
        
        return 0
        
    except ValueError as e:
        print(f"[错误] {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"[错误] 生成视频时出错: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())

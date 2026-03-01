#!/usr/bin/env python3
"""
卓然自拍技能 - OpenClaw 兼容入口
支持命令行调用和模块导入
"""

import os
import sys
import json
import argparse

# 确保能找到技能模块
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(SCRIPT_DIR, '..'))

from zhuoran_selfie import generate_smart, generate_one_step, generate_two_step, SCENE_TEMPLATES, DISABLED_SCENES

def main():
    parser = argparse.ArgumentParser(
        description='卓然自拍技能 - 生成场景化自拍照片',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
示例:
  # 智能模式生成办公室自拍
  python3 zhuoran-selfie.py office
  
  # 指定自拍模式
  python3 zhuoran-selfie.py cafe --mode selfie
  
  # 使用两步法（高质量）
  python3 zhuoran-selfie.py beach --method two_step
  
  # 生成并发送到指定频道
  python3 zhuoran-selfie.py gym --target "@username"

可用场景:
  office, cafe, airport, westlake, bookstore, gym, beach, selfie_late_night
        '''
    )
    
    parser.add_argument(
        'scene',
        choices=list(SCENE_TEMPLATES.keys()),
        help='场景名称'
    )
    
    parser.add_argument(
        '--mode', '-m',
        choices=['direct', 'selfie', 'portrait'],
        default='direct',
        help='生成模式 (默认: direct)'
    )
    
    parser.add_argument(
        '--method',
        choices=['one_step', 'two_step', 'smart'],
        default='smart',
        help='生成方法 (默认: smart)'
    )
    
    parser.add_argument(
        '--target', '-t',
        help='发送目标（可选，如 @username 或 #channel）'
    )
    
    parser.add_argument(
        '--caption', '-c',
        default='',
        help='图片配文（可选）'
    )
    
    parser.add_argument(
        '--output', '-o',
        help='输出文件路径（可选，默认保存到 /tmp）'
    )
    
    args = parser.parse_args()
    
    # 检查禁用场景
    if args.scene in DISABLED_SCENES:
        print(f"❌ 场景 '{args.scene}' 已被禁用（高风险场景，避免使用）")
        sys.exit(1)
    
    # 选择生成方法
    print(f"🎯 场景: {args.scene}")
    print(f"📷 模式: {args.mode}")
    print(f"⚙️  方法: {args.method}")
    print()
    
    if args.method == 'one_step':
        image_url = generate_one_step(args.scene, args.mode)
    elif args.method == 'two_step':
        image_url = generate_two_step(args.scene, args.mode)
    else:  # smart
        image_url = generate_smart(args.scene, args.mode)
    
    if not image_url:
        print("❌ 生成失败")
        sys.exit(1)
    
    print(f"\n✅ 生成成功: {image_url}")
    
    # 下载图片
    import requests
    
    if args.output:
        output_path = args.output
    else:
        output_path = f"/tmp/zhuoran_{args.scene}_{args.method}.png"
    
    try:
        resp = requests.get(image_url, timeout=30)
        with open(output_path, 'wb') as f:
            f.write(resp.content)
        print(f"💾 已保存: {output_path}")
    except Exception as e:
        print(f"⚠️  保存失败: {e}")
        output_path = None
    
    # 如果指定了目标，发送
    if args.target and output_path:
        print(f"\n📤 发送到: {args.target}")
        # 这里可以集成 OpenClaw 发送
        # 暂时只打印信息
        print(f"   图片: {output_path}")
        if args.caption:
            print(f"   配文: {args.caption}")
        print("   (发送功能需要 OpenClaw CLI 支持)")
    
    # 输出 JSON 结果（便于程序解析）
    result = {
        "success": True,
        "scene": args.scene,
        "mode": args.mode,
        "method": args.method,
        "image_url": image_url,
        "output_path": output_path
    }
    
    print("\n--- JSON 输出 ---")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()

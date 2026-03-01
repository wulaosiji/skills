# -*- coding: utf-8 -*-
"""
配置文件
"""

import os
from pathlib import Path

# 欢迎冷却时间（分钟）
WELCOME_COOLDOWN_MINUTES = 60

# 每批最多@人数
BATCH_SIZE = 20

# 夜间模式（不发送欢迎消息）
NIGHT_MODE_START = 23  # 23:00
NIGHT_MODE_END = 7     # 07:00

# 从 .env 文件读取配置
def load_env_config():
    env_path = Path.home() / '.openclaw' / '.env'
    config = {}
    if env_path.exists():
        with open(env_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    config[key.strip()] = value.strip().strip('"\'')
    return config

env_config = load_env_config()
APP_ID = os.getenv("FEISHU_APP_ID")
APP_SECRET = os.getenv("FEISHU_APP_SECRET")

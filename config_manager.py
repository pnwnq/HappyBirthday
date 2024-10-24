import json
import os

CONFIG_FILE = "config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"volume": 0.7}  # 默认音量为70%

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

def get_volume():
    config = load_config()
    return config.get("volume", 0.7)

def set_volume(volume):
    config = load_config()
    config["volume"] = volume
    save_config(config)

if __name__ == "__main__":
    # 测试配置文件功能
    print("当前音量:", get_volume())
    set_volume(0.8)
    print("设置后音量:", get_volume())

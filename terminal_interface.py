import sys
import time
import random

def type_effect(text, delay=0.05):
    for char in text:
        try:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        except:
            # 如果写入失败，直接打印整行文本
            print(text)
            return
    print()

def display_ascii_art():
    ascii_art = """
    ██   ██  █████  ██████  ██████  ██    ██     ██████  ██ ██████  ████████ ██   ██ ██████   █████  ██    ██ 
    ██   ██ ██   ██ ██   ██ ██   ██  ██  ██      ██   ██ ██ ██   ██    ██    ██   ██ ██   ██ ██   ██  ██  ██  
    ███████ ███████ ██████  ██████    ████       ██████  ██ ██████     ██    ███████ ██   ██ ███████   ████   
    ██   ██ ██   ██ ██      ██         ██        ██   ██ ██ ██   ██    ██    ██   ██ ██   ██ ██   ██    ██    
    ██   ██ ██   ██ ██      ██         ██        ██████  ██ ██   ██    ██    ██   ██ ██████  ██   ██    ██    
    """
    print(ascii_art)

def display_birthday_message():
    messages = [
        "生日快乐，曹羽！",
        "愿你的每一天都充满阳光与笑声！",
        "愿你在新的一岁里收获更多美好的回忆！",
        "永远保持对生活的热情与期待！",
        "祝你心想事成，万事如意！🎂🌟"
    ]
    
    display_ascii_art()
    for message in messages:
        type_effect(message)
        time.sleep(1)

if __name__ == "__main__":
    display_birthday_message()

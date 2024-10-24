import os
import sys
import threading
import pygame

# 添加这些行来确保 pygame 被正确导入
if getattr(sys, 'frozen', False):
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
    os.environ['SDL_VIDEODRIVER'] = 'windib'

import pygame
from wallpaper_generator import generate_wallpaper
from autostart import add_to_startup
from terminal_interface import display_birthday_message
from audio_player import initialize_audio, set_volume, audio_player
from gui import show_volume_control
from config_manager import get_volume, set_volume as save_volume
import threading

def main():
    # 初始化并播放背景音乐
    initialize_audio()

    # 从配置文件加载音量设置
    initial_volume = get_volume()
    set_volume(initial_volume)

    # 生成并设置壁纸
    generate_wallpaper()

    # 添加程序到开机自启动
    add_to_startup()

    # 在新线程中显示音量控制界面
    volume_control_thread = threading.Thread(target=show_volume_control, args=(initial_volume,))
    volume_control_thread.start()

    # 显示终端风格的祝福界面
    display_birthday_message()

    # 等待用户输入来退出程序
    input("按回车键退出程序...")

    # 停止背景音乐
    audio_player.stop_background_music()

    # 退出程序
    pygame.quit()
    sys.stdout.flush()  # 确保所有输出都被刷新
    os._exit(0)  # 使用 os._exit() 强制退出，避免潜在的清理问题

if __name__ == "__main__":
    main()

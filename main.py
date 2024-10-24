import sys
from wallpaper_generator import generate_wallpaper
from autostart import add_to_startup
from terminal_interface import display_birthday_message
from audio_player import initialize_audio, play_birthday_sound, set_volume
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

    # 播放生日音效
    play_birthday_sound()

    # 在新线程中显示音量控制界面
    volume_control_thread = threading.Thread(target=show_volume_control, args=(initial_volume,))
    volume_control_thread.start()

    # 显示终端风格的祝福界面
    display_birthday_message()

    # 等待音量控制界面关闭
    volume_control_thread.join()

if __name__ == "__main__":
    main()

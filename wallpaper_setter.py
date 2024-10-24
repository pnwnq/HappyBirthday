import ctypes
import os

def set_wallpaper(image_path):
    # 确保图片路径是绝对路径
    abs_image_path = os.path.abspath(image_path)
    
    # 使用Windows API设置壁纸
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_image_path, 0)

if __name__ == "__main__":
    # 假设生成的壁纸图片名为 "birthday_wallpaper.png"
    wallpaper_path = "birthday_wallpaper.png"
    set_wallpaper(wallpaper_path)
    print(f"壁纸已设置为: {wallpaper_path}")

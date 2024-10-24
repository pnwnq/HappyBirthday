import winreg
import os
import sys

def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.abspath(sys.argv[0])
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)
        winreg.SetValueEx(key, "HappyBirthdayCaoYu", 0, winreg.REG_SZ, file_path)
        winreg.CloseKey(key)
        print("程序已添加到开机自启动")
        return True
    except WindowsError:
        print("无法添加程序到开机自启动")
        return False

def remove_from_startup():
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"

    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_ALL_ACCESS)
        winreg.DeleteValue(key, "HappyBirthdayCaoYu")
        winreg.CloseKey(key)
        print("程序已从开机自启动中移除")
        return True
    except WindowsError:
        print("无法从开机自启动中移除程序")
        return False

if __name__ == "__main__":
    add_to_startup()

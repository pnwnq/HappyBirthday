@echo off
cd /d "%~dp0"

rem 清理旧的打包结果
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build
if exist *.spec del /f /q *.spec
if exist HappyBirthdayCaoYu.exe del /f /q HappyBirthdayCaoYu.exe

rem 运行 PyInstaller
pyinstaller --onefile --noconsole --add-data "birthday_icon.ico;." --add-data "assets;assets" --icon=birthday_icon.ico --name "HappyBirthdayCaoYu" --hidden-import=pygame --hidden-import=PIL --hidden-import=tkinter main.py

rem 如果打包成功，将可执行文件移动到当前目录
if exist dist\HappyBirthdayCaoYu.exe (
    move /y dist\HappyBirthdayCaoYu.exe .
    rmdir /s /q dist
    rmdir /s /q build
    del /f /q *.spec
    echo 打包成功，可执行文件已生成：HappyBirthdayCaoYu.exe
) else (
    echo 打包失败，请检查错误信息
)

pause

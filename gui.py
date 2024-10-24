import tkinter as tk
from tkinter import ttk
from audio_player import set_volume
from config_manager import set_volume as save_volume

class VolumeControl(tk.Tk):
    def __init__(self, initial_volume):
        super().__init__()

        self.title("音量控制")
        self.geometry("300x100")

        self.volume = tk.DoubleVar()
        self.volume.set(initial_volume * 100)  # 将0-1的值转换为0-100

        self.create_widgets()

    def create_widgets(self):
        # 创建音量滑块
        volume_slider = ttk.Scale(
            self,
            from_=0,
            to=100,
            orient='horizontal',
            variable=self.volume,
            command=self.update_volume
        )
        volume_slider.pack(pady=20)

        # 创建音量标签
        self.volume_label = ttk.Label(self, text=f"音量: {int(self.volume.get())}%")
        self.volume_label.pack()

    def update_volume(self, *args):
        volume = int(self.volume.get())
        self.volume_label.config(text=f"音量: {volume}%")
        new_volume = volume / 100
        set_volume(new_volume)
        save_volume(new_volume)  # 保存音量设置到配置文件

def show_volume_control(initial_volume):
    app = VolumeControl(initial_volume)
    app.mainloop()

if __name__ == "__main__":
    show_volume_control(0.7)  # 测试用，初始音量设为70%

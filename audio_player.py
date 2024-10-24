import pygame
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class AudioPlayer:
    def __init__(self):
        pygame.mixer.init()
        self.background_music = None
        self.volume = 0.5  # 默认音量为50%

    def load_background_music(self, file_path):
        self.background_music = pygame.mixer.Sound(file_path)
        self.background_music.set_volume(self.volume)

    def play_background_music(self, loops=-1):
        if self.background_music:
            self.background_music.play(loops)

    def stop_background_music(self):
        if self.background_music:
            self.background_music.stop()

    def set_volume(self, volume):
        self.volume = max(0.0, min(1.0, volume))  # 确保音量在0.0到1.0之间
        if self.background_music:
            self.background_music.set_volume(self.volume)

audio_player = AudioPlayer()

def initialize_audio():
    audio_player.load_background_music(resource_path("assets/background_music.mp3"))
    audio_player.play_background_music()

def set_volume(volume):
    audio_player.set_volume(volume)

if __name__ == "__main__":
    initialize_audio()
    input("按回车键停止音乐...")
    audio_player.stop_background_music()

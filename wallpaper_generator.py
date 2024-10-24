import pygame
import random
from wallpaper_setter import set_wallpaper
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

# 初始化Pygame
pygame.init()

# 设置屏幕大小
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# 创建屏幕对象
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# 设置颜色
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# 设置字体
font = pygame.font.Font(resource_path("assets/font.ttf"), 20)

# 创建"代码雨"效果
class CodeRain:
    def __init__(self):
        self.font = pygame.font.Font(resource_path("assets/font.ttf"), 20)
        self.characters = "01"
        self.drops = []
        self.initialize_drops()

    def initialize_drops(self):
        for _ in range(200):  # 增加雨滴数量
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(-SCREEN_HEIGHT, 0)
            speed = random.randint(5, 20)  # 增加速度变化
            length = random.randint(5, 30)  # 添加长度变化
            self.drops.append([x, y, speed, length])

    def update(self):
        for drop in self.drops:
            drop[1] += drop[2]
            if drop[1] > SCREEN_HEIGHT:
                drop[1] = random.randint(-50, 0)
                drop[0] = random.randint(0, SCREEN_WIDTH)
                drop[2] = random.randint(5, 20)  # 重置速度
                drop[3] = random.randint(5, 30)  # 重置长度

    def draw(self, surface):
        for drop in self.drops:
            for i in range(drop[3]):
                char = random.choice(self.characters)
                text = self.font.render(char, True, (0, 255 - i * 8, 0))  # 颜色渐变
                surface.blit(text, (drop[0], drop[1] - i * 15))

# 创建"代码雨"对象
code_rain = CodeRain()

# 主循环
def generate_wallpaper():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 填充黑色背景
        screen.fill(BLACK)

        # 更新并绘制"代码雨"
        code_rain.update()
        code_rain.draw(screen)

        # 添加生日祝福文字
        birthday_font = pygame.font.Font(resource_path("assets/font.ttf"), 72)
        birthday_text = birthday_font.render("Happy Birthday, 曹羽!", True, GREEN)
        text_rect = birthday_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(birthday_text, text_rect)

        # 更新显示
        pygame.display.flip()
        clock.tick(30)  # 限制帧率为30FPS

    # 保存壁纸
    wallpaper_path = "birthday_wallpaper.png"
    pygame.image.save(screen, wallpaper_path)
    pygame.quit()

    # 设置壁纸
    set_wallpaper(wallpaper_path)
    print(f"壁纸已生成并设置: {wallpaper_path}")

if __name__ == "__main__":
    generate_wallpaper()

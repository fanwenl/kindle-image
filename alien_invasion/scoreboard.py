""" 计分相关的类 """
import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    """ 显示得分信息的类 """
    def __init__(self, ai_settings, screen, stats):
        """ 初始化显示得分的属性 """
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # 显示得分信息事使用的字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48, bold=False, italic=False)

        # 准备初始得分图像
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """ 将得分转化为一个图像 """
        # 格式化得分，将得分转化为整数，并且是10的倍数
        rounded_score = int(round(self.stats.score))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

        # 得分显示在屏幕的右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        """ 最高分转化为一个图像 """
        # 格式化最高分，将得分转化为整数，并且是10的倍数
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,self.ai_settings.bg_color)

        # 得分显示在屏幕的中间显示
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top 

    def prep_level(self):
        """ 将等级转化为一个图像 """
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.ai_settings.bg_color)

        # 等级显示在得分的下面
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10 

    def show_score(self):
        """ 显示得分 """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

        # 绘制剩余的飞船
        self.ships.draw(self.screen)

    def prep_ships(self):
        """ 显示余下的多少艘飞船 """
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

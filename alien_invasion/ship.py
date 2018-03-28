""" 飞船显示相关函数 """
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """ 飞船相关的类 """
    def __init__(self, ai_settings, screen): 
        """ 初始化飞船的相关设置 """
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船放在屏幕的底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数、
        self.center = float(self.rect.centerx)

        # 移动标志位
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """ 在制定位置绘制飞船 """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ 根据移动标志位调整飞船的位置 """

        # 限制飞船移动的范围
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # 根据self.center更新rect的对象(这个是不是只会得到整数部分)
        self.rect.centerx = self.center

    def center_ship(self):
        """ 让飞船在屏幕上居中 """
        self.center = self.screen_rect.centerx

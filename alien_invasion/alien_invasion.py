""" 游戏的主文件 """
import pygame
from pygame.sprite import Group
from setting import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    """游戏主函数 """
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建统计信息的实例
    stats = GameStats(ai_settings)

    # 创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个子弹的编组
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建开始按钮
    play_button = Button(ai_settings, screen, "Play")

    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, stats, sb, screen, ship, aliens, bullets, play_button)

run_game()
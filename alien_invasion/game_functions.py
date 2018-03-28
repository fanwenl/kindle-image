""" 游戏的功能函数 """
import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """ 按键按下 """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """ 按键松开 """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets):
    """ 响应按键和鼠标的操作 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 按键按下
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        # 按键松手
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """ 在玩家单击play按钮时开始新游戏 """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and (not stats.game_active):\
        # 重置游戏的设置
        ai_settings.initialize_dynamic_settings()
        # 标记游戏开始
        stats.game_active = True

        # 隐藏光标
        pygame.mouse.set_visible(False)

        # 重置游戏统计信息
        stats.reset_stats()

        # 重置记分的图像
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_score()

        # 显示剩余的飞船
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

def update_screen(ai_settings, stats, sb, screen, ship, aliens, bullets, play_button):
    """ 更新屏幕上的图片，切换到新的屏幕 """
    screen.fill(ai_settings.bg_color)
    # 绘制所有的子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 绘制飞船
    ship.blitme()
    # 绘制外星飞船
    aliens.draw(screen)

    # 显示得分
    sb.show_score()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 最近绘制的显示在屏幕上
    pygame.display.flip()

def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ 更新子弹的位置，删除消失的子弹 """
    bullets.update()
    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)

def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ 响应子弹和外星人的碰撞 """
    # 检查是否有子弹击中外星人，如果是则删除对应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True, collided = None)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            sb.prep_score()
    
    # 检查最高分，以及更新
    check_high_score(stats, sb)

    # 检查外星人是否为空，如果为空:删除现有的子弹，重新新建一群外星人(全部被消灭了)
    if len(aliens) == 0:
        bullets.empty()
        # 加快游戏的速度
        ai_settings.increase_speed()
        # 提高游戏的等级
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """ 如果子弹还没有达到限制，创建一个子弹 """
    # 创建子弹，并加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    """ 计算每一行可以容纳的外星人个数 """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings,ship_height, alien_height):
    """ 计算屏幕可以容纳多少行外星人 """
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def creat_alien(ai_settings, screen, aliens, alien_number, row_number):
    """ 创建一个外星并将其挡在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    """ 创建外星人群 """
    #创建一个外星人，并计算一行可容纳多少个外星人
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height, alien.rect.height)

    # 创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            creat_alien(ai_settings, screen, aliens, alien_number, row_number)

def update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """ 检查外星人是否到了屏幕的边缘，并改变他们的方向 """
    check_fleet_edage(ai_settings, aliens)
    aliens.update()
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens, collided = None):
        ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
    
    # 检查是否有外星人到达屏幕的底端
    check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets)

def ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """ 响应被外星人撞到飞船 """
    if stats.ships_left > 0:
        # 飞船数量减一
        stats.ships_left -= 1

        # 更新剩余飞船的数量
        sb.prep_ships()

        # 清空外星人和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群外星人，并将飞船放到屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_fleet_edage(ai_settings, aliens):
    """ 当所有的外星人到达屏幕的边缘是改变方向 """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """ 下移外星人，并改变其方向 """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_aliens_bottom(ai_settings, stats, screen, sb, ship, aliens, bullets):
    """ 检查是否有外星人到达了屏幕的底端 """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞倒一样进行处理
            ship_hit(ai_settings, stats, screen, sb, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    """ 检查是否产生了最高分 """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

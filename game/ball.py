import pygame
import random
from game.constants import Constants
from game.upgrade import Upgrade


class Ball(pygame.sprite.Sprite):
    #konstruktor piłki - nadania wartości początkowy głównym zmiennym, utworzenie obiektów
    def __init__(self, upgrades):
        super().__init__()
        self.y_pos = Constants.screen_height - 75
        self.x_pos = Constants.screen_width / 2

        self.image = pygame.image.load('assets/ballBlue.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.velocity = [0,0]
        self.rect.center = (self.x_pos, self.y_pos)
        self.x_interval = 1
        self.x_iterator = 1
        self.ball_move = False
        self.impact_sound = pygame.mixer.Sound('sounds/impact.wav')
        self.impact_sound.set_volume(0.1)
        self.impact_sound_two = pygame.mixer.Sound('sounds/impact2.wav')
        self.impact_sound_two.set_volume(0.1)
        self.upgrades = upgrades
        self.upgrade = None
        self.random = 30
        self.ball_freeze = False
        self.ball_freeze_count = 0
        self.ball_bounce_count = 0

    #aktualizacja parametrów piłki
    def update(self):
        if self.y_pos < 11:
            self.velocity[1] = -self.velocity[1]
            self.impact_sound_two.play()

        if self.x_iterator <= Constants.max_ball_interval:
            self.x_iterator +=1
        else:
            self.x_iterator = 1
        if self.x_iterator % self.x_interval == 0:
            if self.x_pos < 11 or self.x_pos > Constants.screen_width - 11:
                self.velocity[0] = -self.velocity[0]
                self.impact_sound_two.play()
            self.x_pos += self.velocity[0]
        self.y_pos += self.velocity[1]

        self.rect.center = (self.x_pos, self.y_pos)
    #reset piłki po utracue życia
    def reset(self):
        self.ball_stop()
        self.y_pos = Constants.screen_height - 75
        self.x_pos = Constants.screen_width / 2
        self.rect.center = (self.x_pos, self.y_pos)

    #funcja obsługująca odbicie piłki od belki i zmiene jej kierunku i kątu odbicia
    def check_collide_paddle(self, paddle):
        if self.rect.colliderect(paddle.rect):
            self.impact_sound.play()
            self.ball_bounce_count +=1
            if abs(self.rect.bottom - paddle.rect.top) < Constants.collision_threshold and self.velocity[1] > 0:
                self.velocity[1] = -self.velocity[1]
                if self.ball_freeze_count < paddle.ball_freeze_max and self.ball_freeze_count % 2 == 0:
                    self.y_pos -= 3
                    self.ball_stop()
                    self.x_interval = 21
                    self.ball_freeze_count +=1

                elif self.ball_freeze_count < paddle.ball_freeze_max:
                    self.ball_freeze_count += 1

                if paddle.rect.centerx - self.rect.centerx > 0 and self.velocity[0] != 0:
                    self.velocity[0] = -1
                elif self.velocity[0] != 0:
                    self.velocity[0] = 1
                if abs(paddle.rect.centerx - self.rect.centerx) > 28:
                    self.x_interval = 1
                elif abs(paddle.rect.centerx - self.rect.centerx) > 20:
                    self.x_interval = 2
                elif abs(paddle.rect.centerx - self.rect.centerx) > 12:
                    self.x_interval = 4
                elif abs(paddle.rect.centerx - self.rect.centerx) > 6:
                    self.x_interval = 6
                elif abs(paddle.rect.centerx - self.rect.centerx) > 3:
                    self.x_interval = 10
                else:
                    self.x_interval = 21

            else:
                self.velocity[0] *= -1

    #spradzanie czy piłka opuściała ekran
    def is_of_screen(self):
        return self.y_pos > Constants.screen_height

    #obługa odbicia piłki od cegły
    def bounce(self, brick):
        if self.rect.colliderect(brick.rect):
            if (abs(self.rect.top - brick.rect.bottom) < Constants.collision_threshold and self.velocity[1] < 0) or (abs(self.rect.bottom - brick.rect.top) < Constants.collision_threshold and self.velocity[1] > 0):
                self.velocity[1] = -self.velocity[1]
            elif (abs(self.rect.right - brick.rect.left) < Constants.collision_threshold and self.velocity[0] > 0) or (abs(self.rect.left - brick.rect.right) < Constants.collision_threshold and self.velocity[0] < 0):
                self.velocity[0] = -self.velocity[0]

        if brick.lives >= 2:
            self.impact_sound.play()
        elif brick.lives == 1:
            self.random = random.randint(0, 50)
            if self.random <= 5:
                self.upgrade = Upgrade(brick.x_pos, brick.y_pos, 1)
                self.upgrades.add_upgrade(self.upgrade)
            elif self.random <= 10:
                self.upgrade = Upgrade(brick.x_pos, brick.y_pos, 2)
                self.upgrades.add_upgrade(self.upgrade)
            elif self.random <= 15:
                self.upgrade = Upgrade(brick.x_pos, brick.y_pos, 3)
                self.upgrades.add_upgrade(self.upgrade)
            elif self.random <=20:
                self.upgrade = Upgrade(brick.x_pos, brick.y_pos, 4)
                self.upgrades.add_upgrade(self.upgrade)

            self.impact_sound_two.play()

    #poruszenie piłki
    def ball_start(self):
        if self.ball_move is False:
            self.velocity = [1,1]
            self.ball_move = True

    #zatrzymanie piłki
    def ball_stop(self):
        if self.ball_move:
            self.velocity = [0,0]
            self.ball_move = False

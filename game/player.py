import pygame
from game.constants import Constants
from game.laser import Laser, Lasers

class Player(pygame.sprite.Sprite):

    #konstruktor belki - nadanie wartości poszatkowych
    def __init__(self, lives, lasers):
        super().__init__()
        self.image = pygame.image.load('assets/paddleBlu.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.y_pos = Constants.screen_height - 50
        self.x_pos = Constants.screen_width/2
        self.rect.center = (self.x_pos, self.y_pos)
        self.lives = lives
        self.game_speed = 320
        self.up_move = False
        self.ball_freeze = False
        self.ball_freeze_max = 0
        self.lose_life_sound = pygame.mixer.Sound('sounds/lose_live.wav')
        self.lose_life_sound.set_volume(0.1)
        self.game_over_sound = pygame.mixer.Sound('sounds/game_over.wav')
        self.game_over_sound.set_volume(0.1)
        self.lasers = lasers
        self.lasers_ammo = 0
        self.lasers_ammo_fired = 0
        self.laser_trigger = False
        self.laser_sound = pygame.mixer.Sound('sounds/laser.wav')
        self.laser_sound.set_volume(0.1)

    #aktualizacja położenia belki
    def update(self):
        if self.x_pos < 52:
            self.x_pos = 52

        if self.x_pos > Constants.screen_width - 52:
            self.x_pos = Constants.screen_width - 52

        self.rect.center = (self.x_pos, self.y_pos)

    #mechanizm utraty życia
    def lose_life(self):
        self.lives -= 1
        if self.lives > 0:
            self.lose_life_sound.play()
        else:
            self.game_over_sound.play()

    #reset ilości żyć
    def reset(self):
        self.lives = Constants.starting_lives
    #obsługa poruszania w lewo
    def move_left(self):
        self.x_pos -= Constants.paddle_speed
    #obsługa poruszania w prawo
    def move_right(self):
        self.x_pos += Constants.paddle_speed
    #obsługa kolizji z bonusem
    def check_upgrade(self, upgrade):
        if upgrade.up_type == 1:
            self.lives += 1
        elif upgrade.up_type == 2 and self.game_speed < 470:
            self.game_speed += 50
        elif upgrade.up_type == 3:
            self.ball_freeze = True
            self.ball_freeze_max += 20
        elif upgrade.up_type == 4:
            self.lasers_ammo += 10

    #obsługa wystrzału lasera
    def laser_fire(self):
        if self.lasers_ammo_fired < self.lasers_ammo and self.laser_trigger:
            self.lasers.add_laser(Laser(self.x_pos - 32, Constants.screen_height - 54))
            self.lasers.add_laser(Laser(self.x_pos + 32, Constants.screen_height - 55))
            self.lasers_ammo_fired += 1
            self.laser_trigger = False
            self.laser_sound.play()






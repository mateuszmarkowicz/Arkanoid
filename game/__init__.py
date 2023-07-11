import pygame
import sys

from game.constants import Constants
from game.player import Player
from game.ball import Ball
from game.bricks import Bricks, BricksTwo, BricksThree, BricksFour, BricksFive
from game.upgrade import Upgrades
from game.laser import Lasers

class Game:
    #główny konstruktor - nadania wartości początkowy głównym zmiennym, utworzenie obiektów
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((Constants.screen_width,Constants.screen_height))
        self.clock = pygame.time.Clock()

        self.bg_color = pygame.Color("black")
        self.font = pygame.font.Font('assets/Kenney Future.ttf',16)
        self.game_over = False
        self.lvl_number = 0
        self.increase_lvl = True

        self.all_sprites = pygame.sprite.Group()
        self.lasers = Lasers(self.all_sprites)
        self.upgrades = Upgrades(self.all_sprites)
        self.player = Player(Constants.starting_lives, self.lasers)
        self.ball = Ball(self.upgrades)


        self.all_sprites.add(self.player, self.ball)

        self.bricks = Bricks(self.all_sprites)
        self.lvl_up_sound = pygame.mixer.Sound('sounds/lvl_up.wav')
        self.lvl_up_sound.set_volume(0.1)
        self.lvl_up_played = False
        self.score = 0

    #reset gry, powrót pod pierwszego poziomu
    def reset(self):
        self.upgrades.upgrades_kill()
        self.game_over = False
        self.player = Player(Constants.starting_lives, self.lasers)
        self.ball = Ball(self.upgrades)

        self.all_sprites.empty()
        self.all_sprites.add(self.player, self.ball)
        self.bricks = Bricks(self.all_sprites)
        self.lvl_up_played = False
        self.score = 0
    #rozpoczęcie drugiego poziomu
    def start_lvl_two(self):
        self.game_over = False
        self.player = Player(self.player.lives, self.lasers)
        self.ball = Ball(self.upgrades)

        self.all_sprites.empty()
        self.all_sprites.add(self.player, self.ball)
        self.bricks = BricksTwo(self.all_sprites)

    #rozpoczynanie kolenych poziomów
    def start_lvl_three(self):
        self.game_over = False
        self.player = Player(self.player.lives, self.lasers)
        self.ball = Ball(self.upgrades)

        self.all_sprites.empty()
        self.all_sprites.add(self.player, self.ball)
        self.bricks = BricksThree(self.all_sprites)

    def start_lvl_four(self):
        self.game_over = False
        self.player = Player(self.player.lives, self.lasers)
        self.ball = Ball(self.upgrades)

        self.all_sprites.empty()
        self.all_sprites.add(self.player, self.ball)
        self.bricks = BricksFour(self.all_sprites)

    def start_lvl_five(self):
        self.game_over = False
        self.player = Player(self.player.lives, self.lasers)
        self.ball = Ball(self.upgrades)

        self.all_sprites.empty()
        self.all_sprites.add(self.player, self.ball)
        self.bricks = BricksFive(self.all_sprites)

    #funcja obsługująca naciskanie klawiszy i wyście z programu
    def handle_events(self):
        keys = pygame.key.get_pressed()
        if self.ball.ball_move==False and self.increase_lvl is False and self.game_over is False and keys[pygame.K_SPACE]:
            self.ball.ball_start()
        if keys[pygame.K_LEFT]:
            self.player.move_left()
        if keys[pygame.K_RIGHT]:
            self.player.move_right()
        if self.game_over and keys[pygame.K_RETURN]:
            self.reset()
        if self.increase_lvl and keys[pygame.K_RETURN]:
            self.score += self.bricks.count*100 - self.ball.ball_bounce_count
            self.lvl_number += 1
            self.increase_lvl = False
            self.lvl_up_played = False
            if self.lvl_number == 2:
                self.start_lvl_two()
            if self.lvl_number == 3:
                self.start_lvl_three()
            if self.lvl_number == 4:
                self.start_lvl_four()
            if self.lvl_number == 5:
                self.start_lvl_five()
            if self.lvl_number == 6:
                pygame.quit()
                sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.laser_trigger = True
                    self.player.laser_fire()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            else:
                self.player.laser_trigger = False

    #funckcja obsługująca aktualizację obiektów i zmiennych
    def update(self):
        if self.ball.is_of_screen():
            self.player.lose_life()
            if self.player.lives <= 0:
                self.game_over = True
                self.lvl_number = 1
                self.lasers = Lasers(self.all_sprites)
            self.ball.reset()

        if self.bricks.lvl_is_done():
            self.increase_lvl = True
            self.ball.ball_stop()
            self.upgrades.upgrades_kill()
            self.lasers = Lasers(self.all_sprites)
            if self.lvl_up_played is False:
                self.lvl_up_sound.play()
                self.lvl_up_played = True

        self.ball.check_collide_paddle(self.player)
        self.bricks.check_collisions(self.ball)
        self.upgrades.check_collisions(self.player)
        self.lasers.check_collisions(self.bricks )
        self.all_sprites.update()
        pygame.display.update()

        self.clock.tick(self.player.game_speed)

    #funcja rysująca obiekty na ekranie i wyświtlająca ekran początkowy i ekrany przejściowe
    def draw(self):
        self.screen.fill(self.bg_color)
        if self.game_over:
            text = self.font.render("Game Over!", True, pygame.Color("white"))
            self.screen.blit(text, (Constants.screen_width / 2 - 75, Constants.screen_height/2))
        elif self.increase_lvl and self.lvl_number == 0:
            self.font = pygame.font.Font('assets/Kenney Future.ttf', 50)
            text = self.font.render("Arkanoid", True, pygame.Color("white"))
            self.screen.blit(text, (Constants.screen_width / 2 - 150, 75))
            self.font = pygame.font.Font('assets/Kenney Future.ttf', 16)
            text2 = self.font.render("Press:", True, pygame.Color("white"))
            self.screen.blit(text2, (75, 150))
            text3 = self.font.render("Left and right arrow -  to move bar", True, pygame.Color("white"))
            self.screen.blit(text3, (75, 200))
            text3 = self.font.render("Space -  fire the laser / to move a ball", True, pygame.Color("white"))
            self.screen.blit(text3, (75, 250))
            text4 = self.font.render("Enter -  start level", True, pygame.Color("white"))
            self.screen.blit(text4, (75, 300))
            text5 = self.font.render("Bricks:", True, pygame.Color("white"))
            self.screen.blit(text5, (75, 350))
            text6 = self.font.render("one live:", True, pygame.Color("white"))
            self.screen.blit(text6, (75, 400))
            text7 = self.font.render("two live:", True, pygame.Color("white"))
            self.screen.blit(text7, (300, 400))
            text8 = self.font.render("indestructible:", True, pygame.Color("white"))
            self.screen.blit(text8, (525, 400))
            text9 = self.font.render("to win - destroy all destructible bricks", True, pygame.Color("white"))
            self.screen.blit(text9, (75, 710))
            self.font = pygame.font.Font('assets/Kenney Future.ttf', 22)
            text10 = self.font.render("press enter to start", True, pygame.Color("white"))
            self.screen.blit(text10, (Constants.screen_width / 2 - 165, 780))
            self.font = pygame.font.Font('assets/Kenney Future.ttf', 16)
            text5 = self.font.render("Upgrades:", True, pygame.Color("white"))
            self.screen.blit(text5, (75, 550))
            text6 = self.font.render("add live:", True, pygame.Color("white"))
            self.screen.blit(text6, (75, 600))
            text7 = self.font.render("speed up:", True, pygame.Color("white"))
            self.screen.blit(text7, (250, 600))
            text8 = self.font.render("freeze ball:", True, pygame.Color("white"))
            self.screen.blit(text8, (425, 600))
            text9 = self.font.render("laser:", True, pygame.Color("white"))
            self.screen.blit(text9, (625, 600))
            brick1 = pygame.sprite.Sprite()
            brick1.image = pygame.image.load('assets/element_red_rectangle.png').convert_alpha()
            brick1.rect = brick1.image.get_rect()
            brick1.rect.center = (100, 450)
            brick2 = pygame.sprite.Sprite()
            brick2.image = pygame.image.load('assets/element_blue_rectangle.png').convert_alpha()
            brick2.rect = brick2.image.get_rect()
            brick2.rect.center = (164, 450)
            brick3 = pygame.sprite.Sprite()
            brick3.image = pygame.image.load('assets/element_purple_rectangle.png').convert_alpha()
            brick3.rect = brick3.image.get_rect()
            brick3.rect.center = (100, 482)
            brick4 = pygame.sprite.Sprite()
            brick4.image = pygame.image.load('assets/element_green_rectangle.png').convert_alpha()
            brick4.rect = brick4.image.get_rect()
            brick4.rect.center = (164, 482)
            brick5 = pygame.sprite.Sprite()
            brick5.image = pygame.image.load('assets/element_grey_rectangle.png').convert_alpha()
            brick5.rect = brick5.image.get_rect()
            brick5.rect.center = (350, 466)
            brick6 = pygame.sprite.Sprite()
            brick6.image = pygame.image.load('assets/element_yellow_rectangle.png').convert_alpha()
            brick6.rect = brick6.image.get_rect()
            brick6.rect.center = (600, 466)

            up1 = pygame.sprite.Sprite()
            up1.image = pygame.image.load('assets/up_red.png').convert_alpha()
            up1.rect = up1.image.get_rect()
            up1.rect.center = (120, 660)

            up2 = pygame.sprite.Sprite()
            up2.image = pygame.image.load('assets/up_blue.png').convert_alpha()
            up2.rect = up2.image.get_rect()
            up2.rect.center = (300, 660)

            up3 = pygame.sprite.Sprite()
            up3.image = pygame.image.load('assets/up_green.png').convert_alpha()
            up3.rect = up3.image.get_rect()
            up3.rect.center = (485, 660)

            up4 = pygame.sprite.Sprite()
            up4.image = pygame.image.load('assets/up_yellow.png').convert_alpha()
            up4.rect = up4.image.get_rect()
            up4.rect.center = (660, 660)

            some_sprites = pygame.sprite.Group()
            some_sprites.add(brick1, brick2, brick3, brick4, brick5,brick6, up1, up2, up3, up4)
            some_sprites.draw(self.screen)

        elif self.increase_lvl and self.lvl_number == 1:
            text = self.font.render("Round two!", True, pygame.Color("white"))
            self.screen.blit(text, (Constants.screen_width / 2 - 75, Constants.screen_height / 2))
        elif self.increase_lvl and self.lvl_number == 2:
            text = self.font.render("Round three!", True, pygame.Color("white"))
            self.screen.blit(text, (Constants.screen_width / 2 - 75, Constants.screen_height / 2))
        elif self.increase_lvl and self.lvl_number == 3:
            text = self.font.render("Round four!", True, pygame.Color("white"))
            self.screen.blit(text, (Constants.screen_width / 2 - 75, Constants.screen_height / 2))
        elif self.increase_lvl and self.lvl_number == 4:
            text = self.font.render("Round five!", True, pygame.Color("white"))
            self.screen.blit(text, (Constants.screen_width / 2 - 75, Constants.screen_height / 2))
        elif self.increase_lvl and self.lvl_number == 5:
            text = self.font.render("YOU WIN!", True, pygame.Color("white"))
            self.screen.blit(text, (Constants.screen_width / 2 - 60, Constants.screen_height / 2-10))
            text2 = self.font.render("YOUR SCORE {}".format(self.score + self.bricks.count * 100 - self.ball.ball_bounce_count), True,pygame.Color("white"))
            self.screen.blit(text2, (Constants.screen_width /2 -110, Constants.screen_height/2 + 40))
        else:
            self.all_sprites.draw(self.screen)

            text = self.font.render("Lives {}".format(self.player.lives), True, pygame.Color("white"))
            self.screen.blit(text, (15, 15))

            text2 = self.font.render("Score {}".format(self.score+self.bricks.count*100-self.ball.ball_bounce_count), True, pygame.Color("white"))
            self.screen.blit(text2, (Constants.screen_width-140,15))
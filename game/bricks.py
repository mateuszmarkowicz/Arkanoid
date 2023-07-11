import pygame
from game.constants import Constants

#lista z ściazkami dojścia do grafik
bricks = [
    'assets/element_grey_rectangle.png',
    'assets/element_blue_rectangle.png',
    'assets/element_green_rectangle.png',
    'assets/element_purple_rectangle.png',
    'assets/element_red_rectangle.png',
    'assets/element_yellow_rectangle.png',
]

#klasa tworząca pierwszy poziom
class Bricks:
    def __init__(self, all_sprites):
        self.all_sprites = all_sprites
        self.all_bricks = pygame.sprite.Group()
        self.color = 0
        self.count = 0

        #ustawianie psozczególnych cegieł
        for r in range(4, Constants.brick_rows+3):
            for c in range(Constants.brick_cols):
                brick = Brick(r, c, self.color)
                self.all_sprites.add(brick)
                self.all_bricks.add(brick)
            self.color += 1

    #obługa kolizja cegieł z piłką
    def check_collisions(self,ball):
        collision_list = pygame.sprite.spritecollide(ball, self.all_bricks, False)
        for brick in collision_list:
            ball.bounce(brick)
            brick.lives = brick.lives - 1
            if brick.lives <= 0:
                brick.kill()
                self.count +=1

    #sprawdzenie czy wszystkie cegły są zbite
    def lvl_is_done(self):
        return self.count >= 60


#klasa tworząca drugi poziom
class BricksTwo:
    def __init__(self, all_sprites):
        self.all_sprites = all_sprites
        self.all_bricks = pygame.sprite.Group()
        self.color = 1
        self.count = 0
        self.col_bricks = 1

        for r in range(2, 13):
            self.color = 1
            for c in range(self.col_bricks):
                brick = Brick(r, c, self.color)
                if self.color == 4:
                    self.color = 1
                else:
                    self.color += 1
                self.all_sprites.add(brick)
                self.all_bricks.add(brick)
            self.col_bricks += 1

        self.color = 0
        for c in range(self.col_bricks):
            brick = Brick(13, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

    # obługa kolizja cegieł z piłką
    def check_collisions(self,ball):
        collision_list = pygame.sprite.spritecollide(ball, self.all_bricks, False)
        for brick in collision_list:
            ball.bounce(brick)
            brick.lives = brick.lives - 1
            if brick.lives <= 0:
                brick.kill()
                self.count +=1

    # sprawdzenie czy wszystkie cegły są zbite
    def lvl_is_done(self):
        return self.count >= 78

#klasa tworząca trzeci poziom
class BricksThree:
    def __init__(self, all_sprites):
        self.all_sprites = all_sprites
        self.all_bricks = pygame.sprite.Group()
        self.color = 0
        self.count = 0

        brick = Brick(3, 6, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        brick = Brick(4, 6, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        brick = Brick(9, 2, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        brick = Brick(9, 4, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)



        brick = Brick(9, 8, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        brick = Brick(9, 10, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        for r in range(9,12):
            brick = Brick(r, 6, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        self.color = 5
        brick = Brick(12, 6, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        brick = Brick(13, 6, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        brick = Brick(13, 5, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        brick = Brick(13, 4, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        brick = Brick(12, 4, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        brick = Brick(14, 5, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        self.color = 1

        for r in range(6,9):
            brick = Brick(r, 2, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for r in range(5, 9):
            brick = Brick(r, 3, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        brick = Brick(4, 4, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        brick = Brick(5, 4, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        brick = Brick(4, 5, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        self.color = 2

        for r in range(6, 9):
            brick = Brick(r, 10, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for r in range(5, 9):
            brick = Brick(r, 9, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        brick = Brick(4, 8, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        brick = Brick(5, 8, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        brick = Brick(4, 7, self.color)
        self.all_sprites.add(brick)
        self.all_bricks.add(brick)

        self.color = 3

        for c in range(5, 8):
            brick = Brick(5, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for r in range(6, 9):
            for c in range(4, 9):
                brick = Brick(r, c, self.color)
                self.all_sprites.add(brick)
                self.all_bricks.add(brick)

    # obługa kolizja cegieł z piłką
    def check_collisions(self,ball):
        collision_list = pygame.sprite.spritecollide(ball, self.all_bricks, False)
        for brick in collision_list:
            ball.bounce(brick)
            brick.lives = brick.lives - 1
            if brick.lives <= 0:
                brick.kill()
                self.count +=1

    # sprawdzenie czy wszystkie cegły są zbite
    def lvl_is_done(self):
        return self.count >= 47

#klasa tworząca czwarty poziom
class BricksFour:
    def __init__(self, all_sprites):
        self.all_sprites = all_sprites
        self.all_bricks = pygame.sprite.Group()
        self.color = 3
        self.count = 0

        for c in range(Constants.brick_cols):
            brick = Brick(3, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        self.color = 0

        for c in range(3):
            brick = Brick(5, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(4,7):
            brick = Brick(5, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(8,11):
            brick = Brick(5, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(3):
            brick = Brick(7, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(4,7):
            brick = Brick(7, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(8,11):
            brick = Brick(7, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(3):
            brick = Brick(13, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(4,7):
            brick = Brick(13, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(8,11):
            brick = Brick(13, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(3):
            brick = Brick(15, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(4,7):
            brick = Brick(15, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(8,11):
            brick = Brick(15, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(1,4):
            brick = Brick(9, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(5,8):
            brick = Brick(9, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(9,12):
            brick = Brick(9, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(1,4):
            brick = Brick(11, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(5,8):
            brick = Brick(11, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(9,12):
            brick = Brick(11, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(1,Constants.brick_cols,2):
            brick = Brick(10, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(0,Constants.brick_cols,2):
            brick = Brick(6, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(0, Constants.brick_cols, 2):
            brick = Brick(14, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        self.color = 2

        for c in range(2,Constants.brick_cols,4):
            brick = Brick(10, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        self.color = 4

        for c in range(1,Constants.brick_cols,4):
            brick = Brick(6, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        self.color = 1

        for c in range(1, Constants.brick_cols, 4):
            brick = Brick(14, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

    # obługa kolizja cegieł z piłką
    def check_collisions(self, ball):
        collision_list = pygame.sprite.spritecollide(ball, self.all_bricks, False)
        for brick in collision_list:
            ball.bounce(brick)
            brick.lives = brick.lives - 1
            if brick.lives <= 0:
                brick.kill()
                self.count += 1

    # sprawdzenie czy wszystkie cegły są zbite
    def lvl_is_done(self):
        return self.count >= 93

#klasa tworząca piąty poziom
class BricksFive:
    def __init__(self, all_sprites):
        self.all_sprites = all_sprites
        self.all_bricks = pygame.sprite.Group()
        self.color = 5
        self.count = 0

        for c in range(3, Constants.brick_cols):
            brick = Brick(5, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(8):
            brick = Brick(9, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(3, Constants.brick_cols):
            brick = Brick(13, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        self.color = 2
        for c in range(Constants.brick_cols):
            brick = Brick(3, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        self.color = 3
        for c in range(Constants.brick_cols):
            brick = Brick(7, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        self.color = 1
        for c in range(Constants.brick_cols):
            brick = Brick(11, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        self.color = 0
        for c in range(Constants.brick_cols):
            brick = Brick(15, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        self.color = 4
        for c in range(3):
            brick = Brick(5, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(3):
            brick = Brick(13, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

        for c in range(8, Constants.brick_cols):
            brick = Brick(9, c, self.color)
            self.all_sprites.add(brick)
            self.all_bricks.add(brick)

    # obługa kolizja cegieł z piłką
    def check_collisions(self, ball):
        collision_list = pygame.sprite.spritecollide(ball, self.all_bricks, False)
        for brick in collision_list:
            ball.bounce(brick)
            brick.lives = brick.lives - 1
            if brick.lives <= 0:
                brick.kill()
                self.count += 1

    # sprawdzenie czy wszystkie cegły są zbite
    def lvl_is_done(self):
        return self.count >= 58


class Brick(pygame.sprite.Sprite):
    #konstruktor pojedyńczeń cegły - ustalenie koloru, wiersza i kolumny cegły
    def __init__(self, row, col, color):
        super().__init__()
        self.x_pos = Constants.brick_start + (col * 64) + 32
        self.y_pos = Constants.brick_start + (row * 32) + 16
        self.image = pygame.image.load(bricks[color])
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_pos, self.y_pos)
        if color == 5:
            self.lives = 999
        elif color == 0:
            self.lives = 2
        else:
            self.lives = 1

    #obsługa zderzenia laseru z cegłami
    def laser_damage(self,bricks):
        self.lives -= 1
        if self.lives <= 0:
            self.kill()
            bricks.count += 1






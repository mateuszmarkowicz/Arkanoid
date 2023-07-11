import pygame


class Lasers(pygame.sprite.Sprite):
    #konstruktor laserów - zbioru wszystkich aktualnie isniejących
    def __init__(self, all_sprites):
        super().__init__()
        self.all_sprites = all_sprites
        self.all_lasers = pygame.sprite.Group()
        self.laser_hit_sound = pygame.mixer.Sound('sounds/laser_hit.wav')
        self.laser_hit_sound.set_volume(0.05)

    #dodanie laseru do grup
    def add_laser(self, upgrade):
        self.all_sprites.add(upgrade)
        self.all_lasers.add(upgrade)

    #sprawdzenie i obsługa kolizji wszystkich laserów z wszystkimi cegłami
    def check_collisions(self, bricks):
        collision_dictionary= pygame.sprite.groupcollide(self.all_lasers, bricks.all_bricks, False, False)
        for laser, bricks_two in collision_dictionary.items():
            for brick in bricks_two:
                laser.kill()
                brick.laser_damage(bricks)
                self.laser_hit_sound.play()

class Laser(pygame.sprite.Sprite):
    #konstruktor lasera - ustalenie położenia, obrazka i prędkości
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.image = pygame.image.load('assets/laser.png').convert_alpha()

        self.rect = self.image.get_rect()

        self.y_velocity = -1
        self.rect.center = (self.x_pos, self.y_pos)

    #funcja aktualizujaca położenie lasera
    def update(self):
        self.y_pos += self.y_velocity
        self.rect.center = (self.x_pos, self.y_pos)
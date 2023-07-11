import pygame


class Upgrades(pygame.sprite.Sprite):
    # konstruktor bonusów - zbioru wszystkich aktualnie isniejących
    def __init__(self, all_sprites):
        super().__init__()
        self.all_sprites = all_sprites
        self.all_upgrades = pygame.sprite.Group()
        self.power_up_sound = pygame.mixer.Sound('sounds/powerup.wav')
        self.power_up_sound.set_volume(0.1)

    #dodanie bonusu do grup
    def add_upgrade(self, upgrade):
        self.all_sprites.add(upgrade)
        self.all_upgrades.add(upgrade)

    #sprawdzenie kolizji z belką
    def check_collisions(self, paddle):
        collision_list = pygame.sprite.spritecollide(paddle, self.all_upgrades, False)
        for upgrade in collision_list:
            upgrade.kill()
            self.power_up_sound.play()
            paddle.check_upgrade(upgrade)

    #zniszczenie bonusu
    def upgrades_kill(self):
        for upgrade in self.all_upgrades:
            upgrade.kill()


class Upgrade(pygame.sprite.Sprite):
    # konstruktor bonusu, nadanie połóżenia i ustalenie typu bonusu
    def __init__(self, x_pos, y_pos, up_type):
        super().__init__()
        self.y_pos = y_pos
        self.x_pos = x_pos
        self.up_type = up_type


        if self.up_type == 1:
            self.image = pygame.image.load('assets/up_red.png').convert_alpha()
        elif self.up_type == 2:
            self.image = pygame.image.load('assets/up_blue.png').convert_alpha()
        elif self.up_type == 3:
            self.image = pygame.image.load('assets/up_green.png').convert_alpha()
        elif self.up_type == 4:
            self.image = pygame.image.load('assets/up_yellow.png').convert_alpha()

        self.rect = self.image.get_rect()

        self.y_velocity = 1
        self.rect.center = (self.x_pos, self.y_pos)

        self.impact_sound = pygame.mixer.Sound('sounds/powerup.wav')
        self.impact_sound.set_volume(0.1)

    #funcja aktualizująca położenie bonusu
    def update(self):
        self.y_pos += self.y_velocity
        self.rect.center = (self.x_pos, self.y_pos)






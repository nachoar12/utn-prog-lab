import pygame
from settings import TILE_SIZE, SCREEN_WIDTH, projectile_fx, sfx_on
from class_Projectile import Projectile


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        pygame.sprite.Sprite.__init__(self)
        self.animation_speed = 8  # Adjust as needed for animation speed
        self.index = 0
        self.images_right = self.load_animations('run', 4)
        self.images_left = self.load_animations('run', 4, 'left')
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = x
        self.move_direction = 1
        self.move_counter = 0
        self.screen = screen
        self.projectile_group = pygame.sprite.Group()
        self.projectile_path = './assets/img/projectile/grey_ball.png'
        self.projectile_cooldown = 120
        self.projectile_timer = 0
        global sfx_on

    def load_animations(self, action:str, number_of_frames, direction:str = 'right'):
        list_of_frames = []
        for i in range(0,number_of_frames - 1):
            img = pygame.image.load(f'./assets/img/enemy/{action}_{i}.png')
            img = pygame.transform.scale(img, (TILE_SIZE // 2, TILE_SIZE))
            if direction == 'left':
                img = pygame.transform.flip(img, True, False)
            list_of_frames.append(img)
        return list_of_frames

    def update(self, game_over, sfx):
        # Movement and animation logic
        self.index += 1
        if self.index >= len(self.images_right) * self.animation_speed:
            self.index = 0

        # Set the image based on the movement direction
        if self.move_direction < 0:
            self.image = self.images_left[self.index // self.animation_speed % len(self.images_left)]
        elif self.move_direction > 0:
            self.image = self.images_right[self.index // self.animation_speed % len(self.images_right)]

        # Move the enemy
        self.rect.x += self.move_direction
        # debug
        # pygame.draw.rect(self.screen, ('red'), self.rect, 2)
        if self.rect.x - self.start_x <= -50 or self.rect.x - self.start_x >= 50:
            self.move_direction *= -1

        self.projectile_timer += 1
        if self.projectile_timer >= self.projectile_cooldown:
            self.projectile_timer = 0
            enemy_projectile = Projectile(self.rect.centerx, self.rect.centery, self.move_direction, self.projectile_path, 15, 15, 4)
            self.projectile_group.add(enemy_projectile)
            if sfx:
                projectile_fx.play()

        # Update enemy projectiles
        self.projectile_group.update()

        # remove off-screen projectiles
        # for projectile in self.projectile_group:
        #     if projectile.rect.x < 0 - projectile.width or projectile.rect.x > SCREEN_WIDTH + projectile.width:
        #         projectile.kill()

        # Draw enemy projectiles
        self.projectile_group.draw(self.screen)
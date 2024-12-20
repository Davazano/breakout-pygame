from settings import *
from random import choice, uniform


class Paddle(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        
        self.width = GRID_SIZE * 4
        self.height = GRID_SIZE
        self.color = ORANGE
        self.speed = BALL_SPEED
        
        self.image = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        pygame.draw.rect(self.image, self.color, pygame.FRect((0,0), [self.width, self.height]), 0, 20)
        # self.image.fill(ORANGE)

        self.rect = self.image.get_frect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - (GRID_SIZE * 2)))
        self.old_rect = self.rect.copy()
        self.direction = 0

    def move(self, dt):
        self.rect.centerx += self.direction * self.speed * dt
        # print(self.rect.centerx)
        
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
             self.rect.right = SCREEN_WIDTH



    def get_direction(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = -1
        elif keys[pygame.K_RIGHT]:
            self.direction = 1 
        else:
            self.direction = 0
        # self.direction = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        
        # print(self.direction)

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.get_direction()
        self.move(dt)

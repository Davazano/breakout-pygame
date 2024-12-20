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
        

    def update(self, dt):
        pass
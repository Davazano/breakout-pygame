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


class Ball(pygame.sprite.Sprite):
    def __init__(self, group, paddle_sprite):
        super().__init__(group)
        self.paddle_sprite = paddle_sprite
        self.radius = GRID_SIZE // 2
        self.center = [self.radius, self.radius]
        self.color = DARK_ORANGE
        self.speed = BALL_SPEED
        self.out_of_bounds = False

        self.image = pygame.Surface((GRID_SIZE, GRID_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, self.center, self.radius)
        
        self.rect = self.image.get_frect(center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.old_rect = self.rect.copy()
        # for x rnadom choice between left or right
        # for y random choice between two floating point values that always go down
        self.direction = pygame.Vector2(choice((1,-1)), uniform(0.7, 0.8))
        
    
    def move(self, dt):
        # self.rect.center += self.direction * self.speed * dt
        self.rect.x += self.direction.x * self.speed * dt
        self.collision("horizontal")
        self.rect.y += self.direction.y * self.speed * dt
        self.collision("vertical")


    def collision(self, directiion):
        for sprite in self.paddle_sprite:
            if sprite.rect.colliderect(self.rect):
                if directiion == 'horizontal':
                    # print("collision horizontal")
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                        self.direction.x *= -1
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                        self.direction.x *= -1
                else:
                    # print("collision veritcal")
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                        self.direction.y *= -1
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                        self.direction.y *= -1
                        self.out_of_bounds = True
                    

    
    def check_wall_collision(self):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1

        if self.rect.left <= 0:
            self.rect.left = 0
            self.direction.x *= -1

        if self.rect.right >= SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
            self.direction.x *= -1

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.out_of_bounds = True

    
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.move(dt)
        self.check_wall_collision()

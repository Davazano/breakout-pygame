from settings import *
from entities import *

class GameApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        
        self.clock = pygame.time.Clock()
        self.run_game = True
        self.score = 0

        # sprites
        self.all_sprites = pygame.sprite.Group()
        self.paddle_sprite = pygame.sprite.Group()        
        self.ball_sprite = pygame.sprite.Group()
        
        self.paddle = Paddle((self.all_sprites, self.paddle_sprite))
        self.ball = Ball((self.all_sprites, self.ball_sprite), self.paddle_sprite)



    def end_game(self):
        self.run_game = False
        pygame.quit()
        sys.exit()


    def game_over(self):
        my_font = pygame.font.SysFont('Arial', 50)
        game_over_surface = my_font.render('GAME OVER!', True, DARK_ORANGE, LIGHT_GRAY)
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT/4)

        # blit will draw the text on screen
        self.screen.blit(game_over_surface, game_over_rect)
        pygame.display.flip()
        # after 5 seconds we will quit the program
        time.sleep(5)            
        self.end_game()


    def run(self):
        while self.run_game:
            dt = self.clock.tick(FPS) / 1000            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end_game()

            # update
            self.all_sprites.update(dt)

            if self.ball.out_of_bounds == True:
                self.game_over()

            # draw
            self.screen.fill(TEAL)
            self.all_sprites.draw(self.screen)

            pygame.display.update()
            # self.clock.tick(FPS)


if __name__ == "__main__":
    game = GameApp()
    game.run()
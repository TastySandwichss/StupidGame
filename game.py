import pygame
from paddle import *
from ball import *

class Game():

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))
        self.bg = pygame.image.load("images/bg.jpeg")
        self.bg = pygame.transform.scale(self.bg, (800, 600))

        #paddle        
        self.paddle = pygame.image.load("images/paddle.png")
        self.paddle = pygame.transform.scale(self.paddle, (96,30))
        self.player = Paddle(self.window, 350, 450, self.paddle)

        #ball
        self.ball = pygame.image.load("images/ball.png")
        self.ball = pygame.transform.scale(self.ball, (32,32))
        self.superball = Ball(self.window, 378, 278, self.ball)
        
        
        #time
        self.clock = pygame.time.Clock()


    def run(self):

        running = True
        while (running):

            delta_time = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            #render
            self.window.blit(self.bg, (0, 0))
            self.player.draw()
            self.superball.draw()
            self.superball.move(delta_time)
            self.player.move(delta_time)
            self.player.check_wall()
            self.superball.touch_wall()
            
            pygame.display.update()


game = Game()
game.run()

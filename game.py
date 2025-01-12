import pygame
from paddle import *
from ball import *
from block import *

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

        #block
        self.blocks = []

        self.block = pygame.image.load("images/pink_block.png")
        self.block = pygame.transform.scale(self.block, (50,25))
        for y in self.cal_y_pos():
            for x in self.cal_x_pos():
                self.blocks.append(Block(self.window, self.block, x, y))

        
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
            
            for block in self.blocks:
                block.draw()
            pygame.display.update()

    def cal_x_pos(self):
        block_w = self.block.get_width()
        gap = 15
        total_block = self.window.get_width() // (block_w + gap)
        side_gap = (self.window.get_width() - (block_w + gap) * total_block + gap) / 2

        lst = []
        for x in range(total_block):
            lst.append(side_gap + (block_w + gap) * x)

        return lst
    def cal_y_pos(self):
        block_h = self.block.get_height()
        gap = 15
        row = 5

        lst = []
        for y in range(row):
            lst.append(gap + (block_h + gap) * y)

        return lst

game = Game()
game.run()

import pygame

class Block():

    def __init__(self, window, image, x, y):
        self.window = window
        self.image = image
        self.block_rect = self.image.get_rect(x = x, y = y)

    def draw(self):
        self.window.blit(self.image, (self.block_rect.x, self.block_rect.y))
         
    
import pygame
from random import *

class Ball():
    
    def __init__(self, window, x, y, image):
        self.window = window
        self.image = image
        self.ball_rect = self.image.get_rect(x=x, y=y)
        
        self.velocity_x = randint(-200,200)
        self.velocity_y = 150
        
    def draw(self):
        self.window.blit(self.image, (self.ball_rect.x, self.ball_rect.y))
        
    def move(self, delta_time):
        self.ball_rect.y -= self.velocity_y * delta_time
        self.ball_rect.x += self.velocity_x * delta_time
        
    def touch_wall(self):
        if self.ball_rect.x <= 0:
            self.ball_rect.x = 0
            self.velocity_x *= -1
        if self.ball_rect.x >= 750:
            self.ball_rect.x = 750
            self.velocity_x *= -1
        if self.ball_rect.y <= 0:
            self.ball_rect.y = 0
            self.velocity_y *= -1
        if self.ball_rect.y >= 550:
            self.ball_rect.y = 550
            self.velocity_y *= -1
        
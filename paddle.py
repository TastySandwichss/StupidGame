import pygame

class Paddle():

    def __init__(self, window,x, y, image):
        self.window = window
        self.image = image
        self.paddle_rect = self.image.get_rect(x = x, y = y)

        self.velocity = 200

    def draw(self):
        self.window.blit(self.image, (self.paddle_rect.x, self.paddle_rect.y))

    def move(self, delta_time):
        pressed = pygame.key.get_pressed()

        if (pressed[pygame.K_a]):
            self.paddle_rect.x -= self.velocity * delta_time
        if (pressed[pygame.K_LEFT]):
            self.paddle_rect.x -= self.velocity * delta_time
        if (pressed[pygame.K_RIGHT]):
            self.paddle_rect.x += self.velocity * delta_time
        if (pressed[pygame.K_d]):
            self.paddle_rect.x += self.velocity * delta_time
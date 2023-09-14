import pygame
from pygame.locals import *
import random



class Ball():
    def __init__(self, window, window_width, window_height):
        self.window = window
        
        self.image = pygame.image.load("Week0/Images/ball.png")
        ball_rect = self.image.get_rect()
        self.width = ball_rect[2]
        self.height = ball_rect[3]

        self.max_width = window_width - self.width
        self.max_height = window_height - self.height

        self.x = random.randrange(0, self.max_width)
        self.y = random.randrange(0, self.max_height)
        
        speeds_list = [-4, -3, -2, -1, 1, 2, 3, 4]
        self.x_speed = random.choice(speeds_list)
        self.y_speed = random.choice(speeds_list)


    def update(self):

        if self.x not in range(0, self.max_width):
            self.x_speed *= -1
        if self.y not in range(0, self.max_height):
            self.y_speed *= -1

        self.x += self.x_speed
        self.y += self.y_speed

    
    def draw(self):
        self.window.blit(self.image, (self.x, self.y))


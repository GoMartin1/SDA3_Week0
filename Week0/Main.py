import pygame
from pygame.locals import *
import sys
from Ball import *



BLACK = (0, 0, 0)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
FRAMES_PER_SECOND = 30



def main():

    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()

    ball = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ball.update()

        window.fill(BLACK)
        
        ball.draw()
        
        pygame.display.update()
        clock.tick(FRAMES_PER_SECOND)



if (__name__ == "__main__"):
    main()


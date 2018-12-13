import pygame, sys
from pygame.locals import *
import brick
import paddle
import random

class Paddle(pygame.sprite.Sprite):
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
def main():
    # Constants that will be used in the program

    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH = (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    INDIGO = (63, 0, 255)
    VIOLET = (238, 130, 238)
    BLUE = (0, 0, 255)
    GOLD = (255, 209, 63)

    colors = [RED, RED, ORANGE, ORANGE, YELLOW, YELLOW, GREEN, GREEN, CYAN, CYAN]
    whites = [WHITE]

    pygame.init()
    mainSurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    pygame.display.set_caption("Bricks")
    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)

    x = 0
    y = BRICK_Y_OFFSET

    q = PADDLE_Y_OFFSET
    r = (APPLICATION_WIDTH/2)
    bigballer = paddle.Paddle(PADDLE_WIDTH, PADDLE_HEIGHT, whites)
    bigballer.rect.x = r
    bigballer.rect.y = q
    mainSurface.blit(paddle.image, paddle.rect)
    pygame.display.update()


    for m in range(BRICKS_PER_ROW):
        x = 0
        color = colors[m]
        for b in range(BRICKS_PER_ROW):
            bricks = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, color)
            bricks.rect.x = x
            bricks.rect.y = y
            mainSurface.blit(bricks.image, bricks.rect)
            x = x + BRICK_WIDTH + BRICK_SEP
            pygame.display.update()
        y = y + BRICK_HEIGHT + BRICK_SEP

    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()

main()

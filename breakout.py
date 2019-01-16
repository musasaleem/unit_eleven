# Name: Musa Saleem
# Date: 1/16/18
# Last Modified: 1/16/18
# Comments: This is the game of breakout that I have created.
# It is exactly like the classic game of breakout and I made it myself using pygame.
# I have my main file which is this breakout.py.
# I also have other files that contributed to it that I had to import, just to keep it in simplest form.
# The other files are paddle.py, brick.py, ball.py and block.py.
# This is going to be a part of my final project.
# Which is going to be changing the bricks and ball and replacing it with images and sounds instead.


import pygame, sys
from pygame.locals import *
import brick
import paddle
import ball


def main():
    # Constants that will be used in the program

    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
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

    # Defining variables in replace for big names
    q = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    r = (APPLICATION_WIDTH/2)

    # Defining terms for the paddle and variables for it, bigballer = paddle, and then bliting it to display it
    bigballer = paddle.Paddle(mainSurface, whites[0], PADDLE_WIDTH, PADDLE_HEIGHT)
    bigballer.rect.x = r
    bigballer.rect.y = q
    mainSurface.blit(bigballer.image, bigballer.rect)
    pygame.display.update()

    # Defining the terms for the bricks and the paddle
    brick_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()
    paddle_group.add(bigballer)
    ballz = ball.Ball(WHITE, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    ballz.rect.y = APPLICATION_HEIGHT/2
    ballz.rect.x = APPLICATION_WIDTH/2

# This is the function that makes the row of bricks at the top of the screen, makes row of bricks in different colors
    for m in range(BRICKS_PER_ROW):
        x = 0
        color = colors[m]
        for b in range(BRICKS_PER_ROW):
            bricks = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, color)
            brick_group.add(bricks)
            bricks.rect.x = x
            bricks.rect.y = y
            mainSurface.blit(bricks.image, bricks.rect)
            x = x + BRICK_WIDTH + BRICK_SEP
            pygame.display.update()
        y = y + BRICK_HEIGHT + BRICK_SEP

# This is a while statement that I put to make sure when the code has to end
    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()
        mainSurface.fill(BLACK)
        for bricks in brick_group:
            mainSurface.blit(bricks.image, bricks.rect)


# this is moving the paddle and moving the ball on the screen
        bigballer.move()
        mainSurface.blit(bigballer.image, bigballer.rect)
        ballz.move()
        mainSurface.blit(ballz.image, ballz.rect)
        pygame.display.update()

# This is the collide method to make the ball collide with the paddle and also the bricks and displays it on breakout
        ballz.collide(brick_group)
        if ballz.rect.bottom >= APPLICATION_HEIGHT:
            ballz.rect.x = 205
            ballz.rect.y = 300
            NUM_TURNS -= 1
            if NUM_TURNS == 0:
                pygame.quit()
                sys.exit()
        ballz.collide_paddle(paddle_group)
        if len(brick_group) == 0:
            pygame.quit()
            sys.exit()


main()
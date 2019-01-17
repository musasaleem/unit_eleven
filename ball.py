
import pygame


class Ball(pygame.sprite.Sprite):

   def __init__(self, color, windowWidth, windowHeight, radius):
       """
       Defining the paramaters of the color, window width and Window Height and Radius of the ball
       :param color: White
       :param windowWidth: WindowWidth
       :param windowHeight: WindowHeight
       :param radius: the radius times 2
       """
       super().__init__()

       self.color = color
       self.radius = radius
       self.windowWidth = windowWidth
       self.windowHeight = windowHeight
       self.speedx = 5
       self.speedy = 5
       self.image = pygame.image.load("Drake.png")
       self.rect = self.image.get_rect()

       #
       pygame.display.update()

   def move(self):
       """
       Moving the ball so it hits off the walls
       :return:
       """
       self.rect.top += self.speedy
       self.rect.left += self.speedx

       if self.rect.top < 0:
           self.speedy = -self.speedy
       elif self.rect.bottom > self.windowHeight:
           self.rect.x = 200
           self.rect.y = 200
       elif self.rect.left < 0 or self.rect.right > self.windowWidth:
           self.speedx = -self.speedx

   def collide(self, brick_group):
       """
       Colliding the ball with the bricks
       :param brick_group:
       :return:
       """
       if pygame.sprite.spritecollide(self, brick_group, True):
           self.speedy = -self.speedy

   def collide_paddle(self, paddle_group):
       """
       Colliding the ball with the paddle
       :param paddle_group:
       :return:
       """
       if pygame.sprite.spritecollide(self, paddle_group, False):
           self.speedy = -self.speedy
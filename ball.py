
import pygame


class Ball(pygame.sprite.Sprite):

   def __init__(self, color, windowWidth, windowHeight, radius):
       super().__init__()

       self.color = color
       self.radius = radius
       self.windowWidth = windowWidth
       self.windowHeight = windowHeight
       self.speedx = 5
       self.speedy = 5
       self.image = pygame.Surface((radius * 2, radius * 2))
       self.image.fill(self.color)
       self.rect = self.image.get_rect()

       pygame.draw.circle(self.image, self.color, (radius, radius), radius, 0)
       pygame.display.update()

   def move(self):
       self.rect.top += self.speedy
       self.rect.left += self.speedx

       if self.rect.top < 0:
           self.speedy = -self.speedy
       elif self.rect.bottom > self.windowHeight:
           self.rect.x = 200
           self.rect.y = 200
       elif self.rect.left < 0 or self.rect.right > self.windowWidth:
           self.speedx = -self.speedx

   def collide(self, paddle_group, brick_group):
       if pygame.sprite.spritecollide(self, brick_group, True):
           self.speedy = -self.speedy
       if pygame.sprite.spritecollide(self, paddle_group, False):
           self.speedy = -self.speedy
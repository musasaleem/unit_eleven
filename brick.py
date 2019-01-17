import pygame

class Brick(pygame.sprite.Sprite):

    def __init__(self, width, height, color):
        # initialize sprite super class
        super().__init__()

        # finish setting the class variables to the parameters
        self.width = width
        self.height = height
        self.color = color

        # Create a surface with the correct height and width
        self.image = pygame.image.load("Supreme.png")
        self.rect = self.image.get_rect()

        # Get the rect coordinates

        # Fill the surface with the correct color

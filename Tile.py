import pygame

class Tile:
    def __init__(self, position, image, canCollide=False, canInteract=False):
        self.position = position
        self.image = pygame.image.load(image)
        self.canCollide = False
        self.canInteract = False
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]

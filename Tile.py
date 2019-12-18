import pygame, random

class Tile:
    def __init__(self, position, image, rot, canCollide=False, canInteract=False):
        self.position = position
        self.rot = rot
        self.image = pygame.image.load(image)
        self.canCollide = canCollide
        self.canInteract = canInteract
        self.rect = self.image.get_rect()
        self.rect.x = position[0]
        self.rect.y = position[1]
        self.image = pygame.transform.rotate(self.image, self.rot)

import pygame

class Item:
    def __init__(self, startPos, itemType):
        self.itemType = itemType
        self.image = pygame.image.load("Images/Items/"+self.itemType+".png")
        self.rect = self.image.get_rect()
        self.rect.x = startPos[0]
        self.rect.y = startPos[1]

    def update(self, parent):
        self.rect.centerx, self.rect.centery = parent.rect.centerx, parent.rect.centery

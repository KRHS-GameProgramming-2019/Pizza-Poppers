import pygame

class Item:
    def __init__(self, location, itemType):
        self.startPos = location
        self.itemType = itemType
        self.image = pygame.image.load("Images/Items/"+self.itemType+".png")
        self.rect = self.image.get_rect()
        self.rect.x = self.startPos[0]
        self.rect.y = self.startPos[1]

    def update(self, parent):
        self.position = [parent.rect.x, parent.rect.y]

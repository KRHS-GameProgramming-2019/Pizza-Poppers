import pygame

class Item:
    def __init__(self, location, itemType):
        self.location = location
        self.itemType = itemType
        self.image = pygame.image.load("Images/Items/"+self.itemType+".png")

    def update(self, parent):
        self.position = [parent.rect.x, parent.rect.y]

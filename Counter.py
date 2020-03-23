import pygame
from Tile import *

class Counter(Tile):
    def __init__(self, position, holding, image="Images/Tiles/cabi.png",canCollide = True):
        self.position = position
        self.holding = holding
        Tile.__init__(self, self.position, image, canCollide, True)

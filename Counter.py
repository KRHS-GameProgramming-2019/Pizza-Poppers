import pygame
from Tile import *

class Counter(Tile):
    def __init__(self, position, holding):
        self.position = position
        self.holding = holding
        Tile.__init__(self, self.position, "Images/Tiles/newtile.png", True, True)

import pygame
from Tile import *

class ChoppingBoard(Tile):
    def __init__(self, position, holding):
        self.position = position
        self.holding = holding
        Tile.__init__(self, self.position, "Images/Tiles/choppingBoard.png", True, True)

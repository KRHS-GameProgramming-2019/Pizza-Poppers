import pygame
from Tile import *

class Trash(Tile):
    def __init__(self, position):
        self.position = position
        Tile.__init__(self, self.position, "Images/Tiles/trash.png", True, True)

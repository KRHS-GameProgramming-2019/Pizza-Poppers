import pygame
from Tile import *

class StockBox(Tile):
    def __init__(self, position, foodType, unlimited):
        self.position = position
        self.foodType = foodType
        self.unlimited = unlimited
        Tile.__init__(self, self.position, "Images/Tiles/stockBox.png", True, True)

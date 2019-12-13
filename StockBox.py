import pygame
from Tile import *

class StockBox(Tile):
    def __init__(self, position, foodType, unlimited):
        self.image = ""
        self.position = position
        self.foodType = foodType
        if self.foodType == "D":
            self.image = "Images/Tiles/stockBox_dough.png"
        if self.foodType == "T":
            self.image = "Images/Tiles/stockBox_tomato.png"
        if self.foodType == "C":
            self.image = "Images/Tiles/stockBox_cheese.png"
        if self.foodType == "M":
            self.image = "Images/Tiles/stockBox_meat.png"
        if self.foodType == None:
            self.image = "Images/Tiles/stockBox_generic.png"
        self.unlimited = unlimited
        Tile.__init__(self, self.position, self.image, True, True)

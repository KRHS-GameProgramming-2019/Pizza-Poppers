import pygame, random, math
from Tile import *
tm = [
"###########",
"#         #",
"#         #",
"#  # #    #",
"#  #+++#  #",
"#    # #  #",
"#         #",
"#         #",
"#         #",
"###########",
]
class TileMap:
    def __init__(self, size, level):
        self.size = size
        self.tiles = []
        self.level = level
        self.loadingMap = False
        self.buildMap()
        
    def readMapFile(self,fileName):
        data = file.open("Levels/"+fileName)
        lines = data.readlines()
        print(lines)

    def buildMap(self):
        y = -1
        for line in tm:
            x=-1
            y+=1
            for char in line:
                x+=1
                print(x,y)
                if char == "-":
                    self.tiles.append(Tile((x*80,y*80), "Images/Tiles/counter.png", False, False))
                if char == "+":
                    self.tiles.append(Tile((x*80,y*80), "Images/Tiles/stove.png", False, False))
                if char == " ":
                    self.tiles.append(Tile((x*80,y*80), "Images/Tiles/tileAlt.png", False, False))
        
    def render(self,screen):
        for tile in self.tiles:
            screen.blit(tile.image, tile.rect)

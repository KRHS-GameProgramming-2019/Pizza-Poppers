import pygame, LevelHandler
from Tile import *
from StockBox import *
from Counter import *
from Trash import *
from DeliveryTable import *
from ChoppingBoard import *
class TileMap:
    def __init__(self, size, level):
        self.size = size
        self.tiles = []
        self.level = level
        self.loadingMap = False
        self.buildMap()

    def buildMap(self):
        mapData = LevelHandler.loadMapFile(self.level)
        mapList = LevelHandler.parseMap(mapData)
        tileData = LevelHandler.parseData(mapData)
        try:
            stockTypes = LevelHandler.getStockBoxes(tileData)
        except:
            stockTypes = []
        boxCount = 0
        y = -1
        for line in mapList:
            x=-1
            y+=1
            for char in line:
                x+=1
                if char == "v":
                    self.tiles.append(Tile((x*80,y*80), "Images/Tiles/stove.png", False, False))
                if char == "s":
                    try:
                        food = stockTypes[boxCount]
                    except:
                        food = None
                    self.tiles.append(StockBox((x*80,y*80), food, True))
                    boxCount += 1
                if char == "-":
                    self.tiles.append(Tile((x*80,y*80), "Images/Tiles/tileAlt.png", False, False))
                if char == "#":
                    self.tiles.append(Counter((x*80,y*80), None))
                if char == "t":
                    self.tiles.append(Trash((x*80,y*80)))
                if char == "d":
                    self.tiles.append(DeliveryTable((x*80,y*80), None))
                if char == "c":
                    self.tiles.append(ChoppingBoard((x*80,y*80), None))
        
    def render(self,screen):
        for tile in self.tiles:
            screen.blit(tile.image, tile.rect)

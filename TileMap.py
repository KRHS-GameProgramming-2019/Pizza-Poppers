import pygame, random, math

class TileMap:
	def __init__(self, size, level):
		self.size = size
		self.tiles = []
		self.level = level
		self.buildMap()

	def buildMap(self):
		self.levelFile = open("Levels/"+self.level+".lvl")
		levelData = self.levelFile.readlines()
		for x in levelData:
			print(x)

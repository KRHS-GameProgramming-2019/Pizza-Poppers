import pygame
from Tile import *

class DeliveryTable(Tile):
	def __init__(self, position, holding):
		self.position = position
		self.holding = holding
		Tile.__init__(self, self.position, "Images/Tiles/deliveryTable.png", True, True)

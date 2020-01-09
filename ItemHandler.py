import pygame
from Item import *
items = []

def sendItem(item,other):
    otherItem = other.holding
    other.holding = item
def deleteItem(item):
	count  = 0
	for i in items:
		count += 1
		if i == item:
			items.remove(count)
def createItem(itemType):
	Item()

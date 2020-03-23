import pygame
from Item import *
items = []

def sendItem(item,other):
    otherItem = other.holding
    other.holding = item
def deleteItem(item):
    count  = -1
    for i in items:
        count += 1
        if i == item:
            items.remove(count)
def createItem(pos, itemType):
    newItem = Item(pos, itemType)
    items.append(newItem)

def renderItems(screen):
    for item in items:
        screen.blit(item.image, item.rect)

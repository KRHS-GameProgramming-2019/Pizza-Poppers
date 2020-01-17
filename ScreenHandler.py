import pygame, TileMap, LevelHandler, Console, ItemHandler
from Player import *
from Conveyor import *

globalScreen = None
currentScreen = None

def init(screen):
    globalScreen = screen
    currentScreen = "title"
    print("PizzaPoppers Initialized")
    screen = pygame.display.set_mode((1260,880))
    pygame.display.set_caption("Pizza Poppers")
    icon = pygame.image.load("Images/icon.png")
    pygame.display.set_icon(icon)

def render():
    if currentScreen == "title":
        

def titleScreen():
    

def gameScreen():
    screen.fill((0,0,0))
    screen.blit(bkg,(0,0))
    cv.animate(screen)
    tileMap.render(screen)
    screen.blit(plr.image,plr.rect)
    ItemHandler.renderItems(screen)

import pygame, TileMap, LevelHandler
from Player import *
pygame.init()
screen = pygame.display.set_mode((1260,880))
pygame.display.set_caption("Pizza Poppers")
icon = pygame.image.load("Images/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
tileMap = TileMap.TileMap(10,"test.lvl")
plr = Player(5,(100,100))
bkg = pygame.image.load("Images/Backgrounds/floor.png")

conveyors = [
pygame.image.load("Images/Backgrounds/Conveyor3.png"),
pygame.image.load("Images/Backgrounds/Conveyor2.png"),
pygame.image.load("Images/Backgrounds/Conveyor1.png")
]

cvRect = conveyors[0].get_rect()
cvRect.x = 960
count = 0
frameCount = 0
while True:
    frameCount += 1
    if count == 2:
        count = 0
    #  Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit();
    #input & calcs
    plr.get_input()
    
    #rendering
    screen.fill((0,0,0))
    screen.blit(bkg,(0,0))
    tileMap.render(screen)
    screen.blit(plr.image,plr.rect)
    if frameCount%5 == 0:
        count += 1
    screen.blit(conveyors[count], cvRect)
    pygame.display.flip()
    clock.tick(60)

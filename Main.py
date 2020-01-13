import pygame, TileMap, LevelHandler, Console, ItemHandler
from Player import *
from Conveyor import *
pygame.init()
screen = pygame.display.set_mode((1260,880))
pygame.display.set_caption("Pizza Poppers")
icon = pygame.image.load("Images/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
tileMap = TileMap.TileMap(10,"test.lvl")
plr = Player(5,(100,100))
bkg = pygame.image.load("Images/Backgrounds/floor.png")
cv = Conveyor(960,800)

while True:
    #  Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit();

    #input & calcs
    plr.get_input()
    Console.listen()
    
    #rendering
    screen.fill((0,0,0))
    screen.blit(bkg,(0,0))
    cv.animate(screen)
    tileMap.render(screen)
    screen.blit(plr.image,plr.rect)
    ItemHandler.renderItems(screen)
    pygame.display.flip()   
    clock.tick(60)

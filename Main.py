import pygame, TileMap, LevelHandler, time
from Player import *
pygame.init()
screen = pygame.display.set_mode((960,880))
pygame.display.set_caption("Pizza Poppers")
icon = pygame.image.load("Images/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
tileMap = TileMap.TileMap(10,"test.lvl")
plr = Player(5,(100,100))
start = time.time()
print (start)

while True:
    now = time.time()-start
    print(now)
    start = time.time()
    #  Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit();
    #plr.get_input()
    tileMap.render(screen)
    screen.blit(plr.image,plr.rect)
    pygame.display.flip()
    clock.tick(60)
    #print(clock.get_fps())

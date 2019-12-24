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

cv1 = pygame.image.load("Images/Backgrounds/Conveyor1.png")
cv1Rect = cv1.get_rect()
cv2 = pygame.image.load("Images/Backgrounds/Conveyor1.png")
cv2Rect = cv1.get_rect()
cv1Rect.x = 960
cv2Rect.x = 960
cv2Rect.y = 800
frameCount = 0
while True:
    frameCount += 1
    #  Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit();
    #input & calcs
    plr.get_input()
    if cv1Rect.y == -800:
        cv1Rect.y = 800
    if cv2Rect.y == -800:
        cv2Rect.y = 800
    #rendering
    screen.fill((0,0,0))
    screen.blit(bkg,(0,0))
    tileMap.render(screen)
    screen.blit(plr.image,plr.rect)
    if frameCount%1 == 0:
        cv1Rect.y -= 1
        cv2Rect.y -= 1
    screen.blit(cv1, cv1Rect)
    screen.blit(cv2, cv2Rect)
    pygame.display.flip()
    clock.tick(60)

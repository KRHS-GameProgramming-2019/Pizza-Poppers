import pygame, TileMap
pygame.init()
screen = pygame.display.set_mode((880,800))
clock = pygame.time.Clock()
tileMap = TileMap.TileMap(10,"test")
while True:
    #  Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit();
    tileMap.render(screen)
    pygame.display.flip()

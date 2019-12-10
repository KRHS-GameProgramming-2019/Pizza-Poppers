import pygame, TileMap
pygame.init()
screen = pygame.display.set_mode((880,800))
clock = pygame.time.Clock()
tileMap = TileMap.TileMap(10,"test")
floor  = pygame.image.load("Images/Backgrounds/PizzaPoppersFloor.png")
floorRect = floor.get_rect()
while True:
    #  Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit();
    screen.blit(floor,floorRect)
    tileMap.render(screen)
    pygame.display.flip()

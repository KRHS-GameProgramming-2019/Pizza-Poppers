import pygame, TileMap
pygame.init()
#pygame.display.set_mode((1000,900))
clock = pygame.time.Clock()
tm = TileMap.TileMap(10,"test")
while True:
	#  Main Event Loop
	while True:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            exit();
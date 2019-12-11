import pygame, TileMap, LevelHandler
pygame.init()
screen = pygame.display.set_mode((960,880))
clock = pygame.time.Clock()
tileMap = TileMap.TileMap(10,"test")

LevelHandler.loadMapFile("test.lvl")

while True:
	#  Main Event Loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit();
	tileMap.render(screen)
	pygame.display.flip()

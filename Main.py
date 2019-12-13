import pygame, TileMap, LevelHandler 
pygame.init()
screen = pygame.display.set_mode((960,880))
pygame.display.set_caption("Pizza Poppers")
icon = pygame.image.load("Images/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
tileMap = TileMap.TileMap(10,"test.lvl")

while True:
	#  Main Event Loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit();
	tileMap.render(screen)
	pygame.display.flip()
	clock.tick(60)

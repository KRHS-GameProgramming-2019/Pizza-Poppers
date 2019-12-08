import pygame
pygame.init()
pygame.display.set_mode((1000,900))
clock = pygame.time.Clock()
while True:
	pygame.display.flip()
	clock.tick()
	while True:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            exit();
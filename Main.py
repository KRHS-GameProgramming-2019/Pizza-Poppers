import pygame
pygame.init()
pygame.display.set_mode((1000,900))
clock = pygame.time.Clock()
while True:
	#  Main Event Loop
	while True:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT:
	            exit();

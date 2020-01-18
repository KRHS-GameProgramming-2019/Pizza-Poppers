import pygame, Console, TileMap
from ItemHandler import *
from Player import *
from Conveyor import *
from Button import *

# Window Setup
pygame.init()
screen = pygame.display.set_mode((1260,880))
pygame.display.set_caption("Pizza Poppers")
icon = pygame.image.load("Images/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
screenState = "Title"
paused = False

# Game Objects
tileMap = TileMap.TileMap(10,"test.lvl")
plr = Player(5,(100,100))
bkg = pygame.image.load("Images/Backgrounds/Floor1.png")
cv = Conveyor(960,800)

# Title Screen Objects
title = pygame.image.load("Images/Backgrounds/TitleScreen1.png")
play = Button((100,250),"Play")
leave = Button((100,350),"Exit")

while True:
	#  Main Event Loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit();
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				if screenState == "Play" or screenState == "Pause":
					paused = not paused
					print(paused)
			
	# Rendering
	Console.listen()
	screen.fill((0,0,0))
	
	if screenState == "Play": # Game Window
		if paused:
			screenState = "Pause"
		else:
			plr.get_input()
			screen.blit(bkg,(0,0))
			cv.animate(screen)
			tileMap.render(screen)
			screen.blit(plr.image,plr.rect)
			renderItems(screen)
	if screenState == "Title": # Title Screen Window
		screen.blit(title,(0,0))
		if play.update():
			screenState = "Play"
		if leave.update():
			exit();
		leave.render(screen)
		play.render(screen)
	if screenState == "Pause": #Paused Screen
		if not paused:
			screenState = "Play"
	pygame.display.flip()   
	clock.tick(60)

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
play = Button((100,250),"Play")
settings = Button((100,350),"Settings")
leave = Button((100,450),"Exit")

# Pause Screen Objects

while True:
	#  Main Event Loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit();
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				if screenState == "Play" or screenState == "Pause":
					paused = not paused
	# Rendering
	Console.listen()
	screen.fill((0,0,0))
	
	if screenState == "Play": # Game Window
		screen.blit(bkg, (0,0))
		if paused:
			screenState = "Pause"
		else:
			plr.get_input()
			cv.animate(screen)
			tileMap.render(screen)
			screen.blit(plr.image,plr.rect)
			renderItems(screen)
	if screenState == "Title": # Title Screen Window
		screen.blit(pygame.image.load("Images/Backgrounds/TitleScreen1.png"), (0,0))
		if play.update():
			screenState = "Play"
		if leave.update():
			exit();
		if settings.update():
			screenState = "Settings"
		settings.render(screen, (100,350))
		leave.render(screen,(100,450))
		play.render(screen)
	if screenState == "Pause": #Paused Screen
		screen.blit(pygame.image.load("Images/Backgrounds/PauseScreen1.png"), (0,0))
		if not paused:
			screenState = "Play"
		if leave.update():
			exit();
		if settings.update():
			screenState = "Settings"
		settings.render(screen, (450,400))
		leave.render(screen,(450,500))
	if screenState == "Settings": # Settings Screen
		pass
	if screenState == "GameSelect": # Game Options Screen
		pass
	pygame.display.flip()   
	clock.tick(60)

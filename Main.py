<<<<<<< Updated upstream
import pygame, TileMap
=======
 import pygame, Console, TileMap
>>>>>>> Stashed changes
from ItemHandler import *
from Player import *
from Conveyor import *
from Button import *
from ImageCycler import *

# Window Setup
pygame.init()
screen = pygame.display.set_mode((1260,720))
pygame.display.set_caption("Pizza Poppers")
icon = pygame.image.load("Images/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
screenState = "Title"
paused = False
fireOnce = True

# Game Objects
tileMap = TileMap.TileMap(10,"test.lvl")
plr = Player(5,(100,100),"Alien")
bkg = pygame.image.load("Images/Backgrounds/Floor1.png")
cv = Conveyor(960,800)

# Title Screen Objects
play = Button((100,250),"Play")
settings = Button((100,350),"Settings")
exitGame = Button((100,450),"Exit")
secret = Button((463,12),"Secret")

# Settings Screen Objects
settingsBkg = pygame.image.load("Images/Backgrounds/SettingsScreen1.png")
back = Button((75,700),"Back")

# Pause Screen Objects
pauseBkg = pygame.image.load("Images/Backgrounds/PauseScreen1.png")
title = Button((450,300),"MainMenu")
resume = Button((450,500),"Resume")

#GameSelect Screen Objects
selectBkg = pygame.image.load("Images/Backgrounds/PauseScreen1.png")
leftSkin = Button((500,250),"LeftButton")
rightSkin = Button((700,250),"RightButton")
skinIcon = ImageCycler((605,250),"Skins")
rightMap = Button((698,400),"RightButton")
leftMap = Button((498,400),"LeftButton")
#mapIcon = None 

while True:
    #  Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit();
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if screenState == "Play" or screenState == "Pause":
                    paused = not paused
    screen.fill((0,0,0))
    
    if screenState == "Play": # Game Window
        if paused:
            screenState = "Pause"
        else:
            screen.blit(bkg, (0,0))
            tileMap.render(screen)
            screen.blit(plr.images[plr.facing], plr.rect)
            plr.get_input()
            cv.animate(screen,1)
            renderItems(screen)
            
    if screenState == "Title": # Title Screen Window
        screen.blit(pygame.image.load("Images/Backgrounds/TitleScreen1.png"), (0,0))
        if play.update():
            screenState = "GameSelect"
        if exitGame.update():
            exit();
        if settings.update():
            back.last = "Title"
            screenState = "Settings"
        if secret.update():
            screenState = "Play"
        settings.render(screen, (100,350))
        exitGame.render(screen,(100,450))
        play.render(screen, (100,250))
        secret.render(screen)
        
    if screenState == "Pause": # Paused Screen
        screen.blit(pauseBkg, (0,0))
        if not paused:
            screenState = "Play"
        if settings.update():
            screenState = "Settings"
            back.last = "Pause"
        if title.update():
            paused = False
            screenState = "Title"
        if resume.update():
            paused = False
        settings.render(screen, (450,400))
        title.render(screen, (450,300))
        resume.render(screen)
        
    if screenState == "Settings": # Settings Screen
        if back.update():
            screenState = back.last
        screen.blit(settingsBkg,(0,0))
        back.render(screen,(75,600))
        
    if screenState == "GameSelect": # Game Options Screen
        screen.blit(selectBkg,(0,0))
        if rightSkin.update():
            skinIcon.changeImage(1)
        if leftSkin.update():
            skinIcon.changeImage(-1)
        if leftMap.update():
            print()
        if rightMap.update():
            print()
        if back.update():
            screenState = "Title"
        if play.update():
            screenState = "Play"
            imgName = skinIcon.imageNames[skinIcon.imagePos]
            name = imgName.split(".")
            plr.rebuildImages(name[0])
        skinIcon.render(screen)
        rightMap.render(screen)
        leftMap.render(screen)
        rightSkin.render(screen)
        leftSkin.render(screen)
        play.render(screen,(675,600))
        back.render(screen,(205,600))
    pygame.display.flip() 
    clock.tick(60)

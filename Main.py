import pygame, TileMap
from ItemHandler import *
from Player import *
from Conveyor import *
from Button import *
from ImageCycler import *
from pygame import mixer as mx
from OrderHandler import *
from Spritesheet import *


# Window Setup
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1260,720))
pygame.display.set_caption("Pizza Poppers")
icon = pygame.image.load("Images/icon.png")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
screenState = "Play"
paused = False
musicPlaying = False
createItem((200,300),"Chicken")
createItem((250,350),"Beef")
createItem((300,100),"Chicken")

order1 = Order("Complete This Order",("foo","bar"))
pbc = mx.Sound("Sound/PBC.ogg")
music1 = mx.Sound("Sound/Music/music3.ogg")
music1.play()

# Game Objects
tileMap = TileMap.TileMap(10,"test.lvl")
plr = Player(5,(100,100),"Alien",1)
plr2 = Player(5,(300,100),"DevSkin",2)
bkg = pygame.image.load("Images/Backgrounds/SteelFloor.png")
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
selectBkg = pygame.image.load("Images/Backgrounds/GameOptionsScreen.png")
leftSkin = Button((500,250),"LeftButton")
rightSkin = Button((700,250),"RightButton")
skinIcon = ImageCycler((605,250),"Skins")
rightSkin2 = Button((698,400),"RightButton")
leftSkin2 = Button((498,400),"LeftButton")
skinIcon2 = ImageCycler((605,400),"Skins")

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
            screen.blit(plr2.images[plr2.facing], plr2.rect)
            plr.get_input()
            plr2.get_input()
            # ~ cv.animate(screen,1)
            renderItems(screen)
            
    if screenState == "Title": # Title Screen Window
        screen.blit(pygame.image.load("Images/Backgrounds/food3.jpg"), (0,0))
        if play.update():
            screenState = "GameSelect"
        if exitGame.update():
            exit(); 
        if settings.update():
            back.last = "Title"
            screenState = "Settings"
        if secret.update():
            pbc.play()
        play.render(screen, (10,605))
        settings.render(screen, (430,605))
        exitGame.render(screen,(850,605))
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
        if rightSkin2.update():
            skinIcon2.changeImage(1)
        if leftSkin2.update():
            skinIcon2.changeImage(-1)
        if back.update():
            screenState = "Title"
        if play.update():
            screenState = "Play"
            imgName = skinIcon.imageNames[skinIcon.imagePos]
            name = imgName.split(".")
            imgName2 = skinIcon2.imageNames[skinIcon2.imagePos]
            name2 = imgName2.split(".")
            plr.rebuildImages(name[0])
            plr2.rebuildImages(name2[0])
        
        skinIcon.render(screen)
        skinIcon2.render(screen)
        leftSkin2.render(screen)
        rightSkin2.render(screen)
        rightSkin.render(screen)
        leftSkin.render(screen)
        play.render(screen,(675,600))
        back.render(screen,(205,600))
    pygame.display.flip() 
    clock.tick(60)

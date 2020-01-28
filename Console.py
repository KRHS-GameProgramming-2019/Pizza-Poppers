# Console for entering commands to test features, spawn items, etc..
import pygame, player
from Tile import *
from ItemHandler import *

def listen():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_BACKQUOTE]:
        command = input("Command: ")
        processCommand(command)

def processCommand(command):
    args = command.split()
    if args[0] == "item":
        if not args[1]:
            print("item usage:")
            print("create - create an item")
        if args[1] == "create":
            if args[2] == "beef":
                createItem([500,500],"beef")
        if args[1] == "list":
            print(items)
    if args[0] == "tile":
        if args[1] == "create":
            print("create tile")
    if args[0] == "player"
        if args[1] == "reskin"
            num = int(args[2])
            skin = args[3]
            player.players[num].rebuildImages(skin)
    if args[0] == "help":
        print("item - manipulate items")
        print("tile - manipulate tiles")
        print("")
    else:
        print("Unknown command, "+str(args[0])+" use help for list of commands")
                

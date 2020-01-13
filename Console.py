# Console for entering commands to test features, spawn items, etc..
import pygame
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
                createItem([300,300],"beef")
        if args[1] == "list":
            print(items)
    if args[0] == "tile":
        if args[1] == "create":
            print("create tile")
    if args[0] == "help":
        print("item - manipulate items")
        print("tile - manipulate tiles")
        print("")
    else:
        print("Unknown command, "+str(args[0])+" use help for list of commands")
                

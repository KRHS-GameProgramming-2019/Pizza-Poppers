# Console for entering commands to test features, spawn items, etc..
import pygame
from Tile import *

def checkInput():
	keys = pygame.key.get_pressed()
	if keys[pygame.K_BACKQUOTE]:
		command = input("Command: ")
		processCommand(command)

def processCommand(command):
	args = command.split()
	if args[0] == "item":
		if args[1] == "create":
			if args[2] == "beef":
				print("beef made")
	if args[0] == "tile":
		if args[1] == "create":
			print("create tile")
	if args[0] == "help":
		print("item - manipulate items")
		print("tile - manipulate tiles")
		print("")
	else:
		print("Unknown command, use help for list of commands")
				

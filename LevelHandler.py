import pygame, math, random

def loadMapFile(fileName):
	mapData = []
	data = open("Levels/"+fileName)
	for line in data:
		for text in line.split():
			mapData.append(text)
	return mapData


def parseMapFile(mapData):
	
	for line in mapData:
		

import pygame, math, random

def loadMapFile(fileName):
	mapData = []
	data = open("Levels/"+fileName)
	for line in data:
		for text in line.split():
			mapData.append(text)
	return mapData


def parseMap(mapData):
	loadingMap = False
	mapList = []
	for line in mapData:
		if line == "end":
			loadingMap = False
		if loadingMap:
			mapList.append(line)
		if line == "map":
			loadingMap = True
	return mapList
	
def parseData(mapData):
	loadingData = False
	dataList = []
	for line in mapData:
		if line == "end":
			loadingData = False
		if loadingData:
			dataList.append(line)
		if line == "data":
			loadingData = True
	return dataList

def 

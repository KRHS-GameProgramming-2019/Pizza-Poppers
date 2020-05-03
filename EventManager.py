import pygame

Managers = []

class EventManager: # Manages Events
	def __init__(self,Name,TickSpeed):
		self.TickSpeed = TickSpeed
		self.Clock = pygame.time.Clock()
		self.TickCounter = 0
		self.Events = []
		Managers.append(self)
	
	def Tick(self):
		for event in self.Events:
			if self.TickCounter%event.Delay == 0:
				if event.Active:
					event.Fire()
		self.Clock.tick(self.TickSpeed)
		self.TickCounter += 1

class Event: # A Frame Based Event
	def __init__(self,Name,Object,Manager,Delay,Active=True):
		self.Name = Name
		self.Manager = Manager
		self.Delay = Delay
		self.Active = Active
		self.Object = Object
		Manager.Events.append(self)
	
	def Fire(self):
		self.Object.Fire(self.Name)

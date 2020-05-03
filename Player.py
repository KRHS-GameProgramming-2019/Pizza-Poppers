import pygame, ItemHandler, TileMap, Animation, os
from EventManager import *

CLIP_SIZE = 96
BORDER_SIZE = 2
FRAMES = 4

players = []

class Player:
	def __init__(self,vel,startPos,skin="GenericCharacter",control=1):
		self.control = control
		self.vel = vel
		self.skin = skin
		
		#Sprite Sheet Animation
		#----
		self.Sheet = pygame.image.load("Images\Spritesheets\GenericCharacter.png").convert()		
		self.Animation = Animation.Animation("GenericCharacter.png",0,4)
		self.AnimationEvent = Event("PlayerAnim",self.Animation,Managers[0],15,True)
		self.Facing = 0
		#-----
		
		self.rect = pygame.Rect((0,0),(CLIP_SIZE,CLIP_SIZE))
		self.rect.x = startPos[0]
		self.rect.y = startPos[1]
		self.fx = 0
		self.fy = 0
		self.facing = 0
		self.holding = None
		self.touching = None
		players.append(self)
			
	def render_frame(self,screen):
		cutRect = self.Animation.Cut
		screen.blit(self.Sheet,self.rect,cutRect)

	def get_input(self):
		keys = pygame.key.get_pressed()
		if self.control == 1: #First Player Control
			if keys[pygame.K_w]:
				self.move(0, -self.vel)
			elif keys[pygame.K_a]:
				self.move(-self.vel, 0)
			elif keys[pygame.K_s]:
				self.move(0, self.vel)
			elif keys[pygame.K_d]:
				self.move(self.vel, 0)
			else:
				self.AnimationEvent.Active = False
			if keys[pygame.K_e]:
				self.interact()
			if keys[pygame.K_q]:
				self.holding = None
			if not self.holding == None:
				self.holding.update(self)
		if self.control == 2: #Second Player Control
			if keys[pygame.K_UP]:
				self.move(0, -self.vel)
			if keys[pygame.K_LEFT]:
				self.move(-self.vel, 0)
			if keys[pygame.K_DOWN]:
				self.move(0, self.vel)
			if keys[pygame.K_RIGHT]:
				self.move(self.vel, 0)
			if keys[pygame.K_KP1]:
				self.interact()
			if keys[pygame.K_KP2]:
				self.drop()
			if not self.holding == None:
				self.holding.update(self)
				
	def move(self, dx, dy):
		if dy < 0: # W
			self.Facing = 1
			self.fy = -1
		if dx > 0: # D
			self.Facing = 2
			self.fx = 1
		if dy > 0: # S
			self.Facing = 0
			self.fy = 1
		if dx < 0: # A
			self.Facing = 3
			self.fx = -1
		self.Animation.Line = self.Facing
		self.AnimationEvent.Active = True

		self.rect.x += dx
		self.rect.y += dy
		for other in TileMap.tms[0].tiles:
			if self.rect.colliderect(other.rect):
				if other.canCollide:
					if dx > 0:
						self.rect.right = other.rect.left
					if dx < 0:
						self.rect.left = other.rect.right
					if dy > 0:
						self.rect.bottom = other.rect.top
					if dy < 0:
						self.rect.top = other.rect.bottom
		for other in players:
			if self.rect.colliderect(other.rect) and not other == self:
				if dx > 0:
					self.rect.right = other.rect.left
				if dx < 0:
					self.rect.left = other.rect.right
				if dy > 0:
					self.rect.bottom = other.rect.top
				if dy < 0:
					self.rect.top = other.rect.bottom
					
	def drop(self):
		self.holding = None
	
	def interact(self):
		if not self.holding:
			for item in ItemHandler.items:
				if self.rect.colliderect(item.rect):
					item.parent = None
					self.holding = item
		else:
			print(1)
			testPos = [self.rect.centerx+(-40*self.fx),self.rect.centery+(-40*self.fy)]
			for tile in TileMap.tms[0].tiles:
				if tile.rect.collidepoint(testPos):
					print(tile)
					tile.holding = self.holding
					self.holding = None

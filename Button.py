import pygame, os
basePath = "Images\Buttons"
class Button:
	def __init__(self, startPos, bType, last=None, toggle=False):
		self.state = 0
		self.isClicked = False
		self.toggle = toggle
		self.last = last
		self.bType = bType
		self.images = [self._buildBtn(""), self._buildBtn("Hover"), self._buildBtn("Click")]
		self.rect = self.images[0].get_rect()
		self.rect.x = startPos[0]
		self.rect.y = startPos[1]

	def _buildBtn(self, suffix):
		return pygame.image.load(os.path.join(basePath,self.bType,"Button"+suffix+".png"))
	
	def update(self, var=None):
		if self.rect.collidepoint(pygame.mouse.get_pos()):
			if pygame.mouse.get_pressed()[0] and not self.isClicked:
				self.state = 2
				self.isClicked = True
				return True
			else:
				self.state = 1
		else:
			self.state = 0
		if not pygame.mouse.get_pressed()[0] and self.isClicked:
			self.isClicked = False
		
	def render(self, screen, customPos=None):
		if customPos:
			self.rect.x = customPos[0]
			self.rect.y = customPos[1]
		screen.blit(self.images[self.state], self.rect)

import pygame

class Spritesheet:
	def __init__(self,file_name):
		self.sprite_sheet = pygame.image.load(file_name).convert()
		
	
	def get_image(self, x, y, w, h):
		image = pygame.Surface([w,h]).convert()
		image.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
		return image
		

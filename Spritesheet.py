import pygame

class Spritesheet:
    def __init__(self,file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
        
    
    def draw_image(self, x, y, sx, sy, w, h, screen):
        image = pygame.Surface([w,h]).convert()
        image.blit(self.sprite_sheet, (0, 0), (sx, sy, w, h))
        
        screen.blit(image,(x,y))
        

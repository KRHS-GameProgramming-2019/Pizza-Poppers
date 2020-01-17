import pygame, os

class Button:
    def __init__(self, startPos, bType):
        self.state = 0
        self.bType = bType
        self.images = [pygame.image.load(os.path.join("Images\Buttons",bType,"Button.png")), pygame.image.load(os.path.join("Images\Buttons",bType,"ButtonHover.png")), pygame.image.load(os.path.join("Images\Buttons",bType,"ButtonClick.png"))]
        self.rect = self.images[0].get_rect()
        self.rect.x = startPos[0]
        self.rect.y = startPos[1]
    
    def update(self, var=None):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.state = 2
                return True
            else:
                self.state = 1
        else:
            self.state = 0
    
    def render(self, screen):
        screen.blit(self.images[self.state], self.rect)

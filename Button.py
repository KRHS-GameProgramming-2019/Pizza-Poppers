import pygame

class Button:
    def __init__(self, startPos, bType):
        self.state = 0
        self.images = [pygame.image.load("Images\Buttons\Play\Button.png"), pygame.image.load("Images\Buttons\Play\ButtonHover.png"), pygame.image.load("Images\Buttons\Play\ButtonClick.png")]
        self.rect = self.images[0].get_rect()
        self.rect.x = startPos[0]
        self.rect.y = startPos[1]
    
    def update(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.state = 2
            else:
                self.state = 1
        else:
            self.state = 0
    
    def render(self, screen):
        screen.blit(self.images[self.state], self.rect)

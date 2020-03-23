import pygame, os
pygame.font.init()
font = pygame.font.SysFont("comicsansms", 25)
class Order:
    def __init__(self, header, goals):
        self.count = 0
        self.headerString = header
        self.goals = []
        self.surface = pygame.image.load("Images/Backgrounds/order.png")
        self.rect = self.surface.get_rect()
        self.surface.fill((255,255,255))
        self.header = font.render(self.headerString, True, (0, 0, 0))
        self.headerRect = self.header.get_rect()
        self.headerRect.x = self.rect.centerx-(self.headerRect.width/2)
        for goalString in goals:
            self.count += 1
            text = font.render(goalString, True, (0, 0, 0))
            rect = text.get_rect()
            rect.x = self.rect.x
            rect.y = self.rect.y
            rect.y += self.count*25
            self.goals.append((text,rect))
            
    def update(self,move,render=False):
        pass
        
    def render(self,screen):
        screen.blit(self.surface, self.rect)
        screen.blit(self.header, self.headerRect)
        for data in self.goals:
            screen.blit(data[0],data[1])
                
        

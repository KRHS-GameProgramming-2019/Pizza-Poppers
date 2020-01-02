import pygame

class Conveyor:
    def __init__(self,x,height):
        self.x = x
        self.height = height
        self.cv1 = pygame.image.load("Images/Backgrounds/Conveyor1.png")
        self.cv1Rect = self.cv1.get_rect()
        self.cv2 = pygame.image.load("Images/Backgrounds/Conveyor1.png")
        self.cv2Rect = self.cv2.get_rect()
        self.cv1Rect.x = x
        self.cv2Rect.x = x
        self.cv2Rect.y = self.height
        self.frameCount = 0
        
    def animate(self, screen):
        self.frameCount += 1
        self.cv1Rect.y -= 1
        self.cv2Rect.y -= 1
        if self.cv1Rect.y == -800:
            self.cv1Rect.y = 800
        if self.cv2Rect.y == -800:
            self.cv2Rect.y = 800
        
        screen.blit(self.cv1, self.cv1Rect)
        screen.blit(self.cv2, self.cv2Rect)
        


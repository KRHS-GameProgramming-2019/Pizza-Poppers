import pygame, os
basePath = "Images\Spritesheets"

class Animation: #Creates and Plays Animation
    def __init__(self, SheetName, Line, Frames):
        self.Sheet = pygame.image.load(os.path.join(basePath,SheetName)) #Spritesheet
        self.cutSize = self.Sheet.get_width()/Frames
        self.Frames = []
        self.Cut = pygame.Rect((0,0),(self.cutSize,self.cutSize))
        self.Length = Frames
        self.Frame = 0
        self.Line = Line
        
    def Fire(self,Event):
        self.Frame += 1
        if self.Frame > self.Length-1:
            self.Frame = 0
        self.Cut = pygame.Rect((self.cutSize*self.Frame,self.cutSize*self.Line),(self.cutSize,self.cutSize))

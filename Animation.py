import Spritesheet, pygame, os
basePath = "Images\Spritesheets"

class Animation: #Creates and Plays Animation
    def __init__(self, Target, SheetName, Line, Frames, Delay):
        self.Sheet = pygame.image.load(os.path.join(basePath,SheetName)) #Spritesheet
        self.Frames = []
        self.Delay = Delay
        self.Length = Frames
        self.Frame = 0
        self.Line = Line
        for x in range(self.Length):
            CutPos = ((x*64),(self.Line*64))
            CutSize = (64,64)
            cut = self.Sheet.load_cut(CutPos,CutSize)
            self.Frames.append(cut)
        
    def Fire(self,Event):
        self.Frame += 1
        if self.Frame > self.Length-1:
            self.Frame = 0

import pygame, os
basePath = "Images/ImageSets"
class ImageCycler:
    def __init__(self, pos, imageSet):
        self.pos = pos
        self.images = []
        self.imageNames = []
        self.imagesLength = 0
        self.imagePos = 0
        self._buildImages(imageSet)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        

    def _buildImages(self,directory):
        images = os.listdir(os.path.join(basePath,directory))
        for img in images:
            print(os.path.join(basePath,directory,img))
            if img[-3:] == "png":
                self.images.append(pygame.image.load(os.path.join(basePath,directory,img)))
                self.imageNames.append(img)
        self.imagesLength = len(self.images)
        self.rect = self.images[0].get_rect()
        
    def changeImage(self, changeValue):
        self.imagePos += changeValue
        if self.imagePos > self.imagesLength-1:
            self.imagePos = 0
        elif self.imagePos < 1:
            self.imagePos = self.imagesLength-1
    
    def render(self,screen):
        screen.blit(self.images[self.imagePos], self.rect)

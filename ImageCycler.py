import pygame, os
basePath = "Images/ImageSets"
class ImageCycler:
    def __init__(self, pos, imageSet):
        self.pos = pos
        self.images = []
        self.imagesLength = 0
        self.imagePos = 0

    def _buildImages(self,directory):
        images = os.listdir(os.path.join(basePath,directory))
        for img in images:
            self.images.append(pygame.image.load(image))
        self.imagesLength = len(self.images)
        self.rect = self.images.get_rect()
        
    def changeImage(self, changeValue):
        self.imagePos += changeValue
        if self.imagePos > self.imagesLength:
            self.imagePos = 0
        elif self.imagePos < 0:
            self.imagePos = self.imagesLength

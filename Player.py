import pygame, ItemHandler, TileMap, os
basePath = "Images\PlayerSkins"
class Player():
    def __init__(self,vel,startPos,skin="Skin1"):
        self.vel = vel
        self.skin = skin
        self.images = [self._buildImage("up"),self._buildImage("down"),self._buildImage("left"),self._buildImage("right")]
        self.rect = self.images[0].get_rect()
        self.rect.x = startPos[0]
        self.rect.y = startPos[1]
        self.facing = 0
        self.holding = None
        self.touching = None
        
    def _buildImage(self,turn):
        return pygame.image.load(os.path.join(basePath,self.skin,turn+".png"))

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(0, -self.vel)
        if keys[pygame.K_a]:
            self.move(-self.vel, 0)
        if keys[pygame.K_s]:
            self.move(0, self.vel)
        if keys[pygame.K_d]:
            self.move(self.vel, 0)
        if keys[pygame.K_e]:
            self.interact()
        if keys[pygame.K_q]:
            self.holding = None

    def move(self, dx, dy):
        if dx > 0:
            self.facing = 3
        if dx < 0:
            self.facing = 2
        if dy > 0:
            self.facing = 1
        if dy < 0:
            self.facing = 0
        self.rect.x += dx
        self.rect.y += dy
        for other in TileMap.tms[0].tiles:
            if self.rect.colliderect(other.rect):
                if other.canCollide:
                    if dx > 0:
                        self.rect.right = other.rect.left
                    if dx < 0:
                        self.rect.left = other.rect.right
                    if dy > 0:
                        self.rect.bottom = other.rect.top
                    if dy < 0:
                        self.rect.top = other.rect.bottom

    def drop(self):
        self.holding = None

    def interact(self):
        pass


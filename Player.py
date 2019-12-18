import pygame, ItemHandler, TileMap

class Player():
    def __init__(self,vel,startPos,image="Images/player.png"):
        self.vel = vel
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = startPos[0]
        self.rect.y = startPos[1]
        self.facing = 1
        self.holding = None
        self.touching = None

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
            self.facing = 1
        if dx < 0:
            self.facing = -1
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


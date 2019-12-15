import pygame

class Player():
    def __init__(self,vel,startPos,image="Images/player.png"):
        self.vel = vel
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = startPos[0]
        self.rect.y = startPos[1]
        self.facing = 1
        self.holding = None

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
            if self.holding != None:
                self.drop()
    
    def collide(self, vel, others):
		for other in others:
			if other.canCollide:
				if self.rect.colliderect(other.rect):
					self.rect.x -= vel[0]
					self.rect.y -= vel[0]

    def move(self, dx, dy):
        if dx > 0:
            self.facing = 1
        if dx < 0:
            self.facing = -1
        self.rect.x += dx
        self.rect.y += dy
        
    def drop(self):
        self.holding = None

    def interact(self):
		pass
		

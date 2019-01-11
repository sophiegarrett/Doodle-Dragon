# character module
import pygame

class Character:
	
	# Initializer
	def __init__(self, xpos, ypos, image):
		self.xpos = xpos
		self.ypos = ypos
		self.image = pygame.image.load(image)
	
	def update(self, xpos, ypos):
		self.xpos = xpos
		self.ypos = ypos
	
	def getX(self):
		return self.xpos
	
	def getY(self):
		return self.ypos
	
	def draw(self, screen):
		screen.fill((255,255,255))
		screen.blit(self.image, (self.xpos, self.ypos))
		pygame.display.flip()
		

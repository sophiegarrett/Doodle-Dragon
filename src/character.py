# character module
import pygame
from pathlib import Path

# general character class
class Character:
	# Initializer
	def __init__(self, xpos, ypos, imagepath):
		self.xpos = xpos
		self.ypos = ypos
		self.image = pygame.image.load(imagepath.resolve().as_posix())
	
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

# player character class
class Player(Character):
	def __init__(self):
		self.imagepath = Path("assets/character/character.gif")
		Character.__init__(self, 50, 50, self.imagepath)
	
	

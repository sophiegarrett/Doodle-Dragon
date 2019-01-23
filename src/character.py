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
		self.x_momentum = 0
		self.y_momentum = 0
	
	def update(self, xpos, ypos):
		self.xpos = xpos
		self.ypos = ypos
	
	def getX(self):
		return self.xpos
	
	def getY(self):
		return self.ypos
	
	def draw(self, screen):
		screen.blit(self.image, (self.xpos, self.ypos))
	
	def moveX(self, distance):
		self.xpos += distance
	
	def moveY(self, distance):
		self.ypos += distance
	
	def getXMomentum(self):
		return self.x_momentum
	
	def getYMomentum(self):
		return self.y_momentum
	
	def stopX(self):
		self.x_momentum = 0
		
	def stopY(self):
		self.y_momentum = 0
	
	def setYMomentum(self, x):
		self.y_momentum = x

# player character class
class Player(Character):
	def __init__(self, floor):
		self.imagepath = Path("assets/character/character.gif")
		Character.__init__(self, 64, floor, self.imagepath)
		self.jumpTick = -1
	
	def run(self, direction):
		if (direction == "right"):
			self.x_momentum = 1
		elif (direction == "left"):
			self.x_momentum = -1
		
	def jump(self):
		self.y_momentum = 3
		self.jumpTick = 120
	
	def checkJump(self):
		return self.jumpTick
	
	def tickJump(self):
		self.jumpTick = self.jumpTick - 1
	
	def stopJump(self):
		self.jumpTick = -1
	

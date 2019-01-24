# character module
import pygame
from pathlib import Path

# general character class
class Character(pygame.sprite.Sprite):
	# Initializer
	def __init__(self, xpos, ypos, width, height, cat):
		# Call the Sprite constructor
		pygame.sprite.Sprite.__init__(self)
		
		# Create an image of the character
		self.category = cat
		self.imagepath = Path("assets/character/" + cat + "/right.png")
		self.image = pygame.Surface([width, height])
		self.image = pygame.image.load(self.imagepath.resolve().as_posix())
		
		# Fetch the rectangle object that has the dimensions of the image
		# Update the position of this object by setting the values of rect.x and rect.y
		self.rect = self.image.get_rect()
		
		self.rect.x = xpos
		self.rect.y = ypos - height
		self.x_momentum = 0
		self.y_momentum = 0
	
	def getX(self):
		return self.rect.x
	
	def getY(self):
		return self.rect.y
	
	def moveX(self, distance):
		self.rect.x += distance
	
	def moveY(self, distance):
		self.rect.y += distance
	
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
	
	def faceRight(self):
		pass
	
	def faceLeft(self):
		pass

# player character class
class Player(Character):
	def __init__(self, floor):
		Character.__init__(self, 64, floor, 100, 64, "player")
		self.jumpTick = -1
	
	def run(self, momentum):
		self.x_momentum = momentum
		
	def jump(self):
		self.y_momentum = 3
		self.jumpTick = 120
	
	def checkJump(self):
		return self.jumpTick
	
	def tickJump(self):
		self.jumpTick = self.jumpTick - 1
	
	def stopJump(self):
		self.jumpTick = -1
	
	def update(self, width, height, floor):
		if (self.x_momentum == 1):
			if (self.rect.x < width-self.rect.width):
				self.moveX(1)
		elif (self.x_momentum == -1):
			if (self.rect.x > 0):
				self.moveX(-1)
		
		if (self.y_momentum >= 1):
			if (self.rect.y > 0):
				self.moveY(-1)
		elif (self.y_momentum <= -1):
			if (self.rect.y < floor - self.rect.height):
				self.moveY(1)
		
		if (self.jumpTick >= 11):
			self.tickJump()
		elif (self.jumpTick >= 1):
			self.tickJump()
			self.setYMomentum(0)
		elif (self.jumpTick == 0):
			self.setYMomentum(-1)
		
		if (self.jumpTick == 0 and self.rect.y == floor - self.rect.height):
			self.stopJump()
	

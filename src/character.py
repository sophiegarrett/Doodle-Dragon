# character module
import pygame
from pathlib import Path

# general character class
class Character(pygame.sprite.Sprite):
	# Initializer
	def __init__(self, xpos, ypos, width, height, cat, face):
		# Call the Sprite constructor
		pygame.sprite.Sprite.__init__(self)
		
		# Load images
		self.category = cat
		self.facing = face
		self.rightpath = Path("assets/character/" + cat + "/right.png")
		self.rightimg = pygame.image.load(self.rightpath.resolve().as_posix())
		self.leftpath = Path("assets/character/" + cat + "/left.png")
		self.leftimg = pygame.image.load(self.leftpath.resolve().as_posix())
		
		# Display the character
		self.image = pygame.Surface([width, height])
		self.image = self.rightimg
		
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
		self.facing = "right"
		self.image = self.rightimg
	
	def faceLeft(self):
		self.facing = "left"
		self.image = self.leftimg

# player character class
class Player(Character):
	def __init__(self, floor):
		Character.__init__(self, 64, floor, 100, 64, "player", "right")
		self.jumpTick = -1
	
	def run(self, momentum):
		self.x_momentum = momentum
		
	def jump(self):
		self.y_momentum = 3
		self.jumpTick = 140
	
	def checkJump(self):
		return self.jumpTick
	
	def tickJump(self):
		self.jumpTick = self.jumpTick - 1
	
	def stopJump(self):
		self.jumpTick = -1
	
	def animate(self):
		pass
	
	def update(self, width, height, floor):
		if (self.x_momentum == 1):
			self.faceRight()
			if (self.rect.x < width-self.rect.width):
				self.moveX(1)
		elif (self.x_momentum == -1):
			self.faceLeft()
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
	

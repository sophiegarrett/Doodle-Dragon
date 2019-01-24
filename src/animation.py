# animation module
import pygame
from pathlib import Path

# animation class
class Animation:
	# Initializer
	def __init__(self, cat):
		self.category = cat

# jump animation class
class Jump(Animation):
	def __init__(self, cat):
		# call the Animation constructor
		Animation.__init__(self, cat)
		
		# Load images
		self.right1path = Path("assets/character/" + cat + "/jump_right_1.png")
		self.right1 = pygame.image.load(self.right1path.resolve().as_posix())
		
		self.right2path = Path("assets/character/" + cat + "/jump_right_2.png")
		self.right2 = pygame.image.load(self.right2path.resolve().as_posix())
		
		self.right3path = Path("assets/character/" + cat + "/jump_right_3.png")
		self.right3 = pygame.image.load(self.right3path.resolve().as_posix())
		
		self.left1path = Path("assets/character/" + cat + "/jump_left_1.png")
		self.left1 = pygame.image.load(self.left1path.resolve().as_posix())
		
		self.left2path = Path("assets/character/" + cat + "/jump_left_2.png")
		self.left2 = pygame.image.load(self.left2path.resolve().as_posix())
		
		self.left3path = Path("assets/character/" + cat + "/jump_left_3.png")
		self.left3 = pygame.image.load(self.left3path.resolve().as_posix())

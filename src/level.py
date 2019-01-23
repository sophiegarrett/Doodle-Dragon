# level module
import pygame
from pathlib import Path

# level class
class Level:
	# Initializer
	def __init__(self, num):
		self.id = num
		self.bgpath = Path("assets/level/" + str(num) + "/background.png")
		self.background = pygame.image.load(self.bgpath.resolve().as_posix())
		
	def display(self, screen):
		screen.blit(self.background, (0,0))
	
	def refresh(self):
		pass

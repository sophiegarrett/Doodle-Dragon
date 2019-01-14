# main module
import pygame
from pathlib import Path
import character

# main class
class App:
	def __init__(self):
		self.running = True
		self.screen = None
		self.size = self.width, self.height = 1024, 576
	
	def on_init(self):
		# initialize pygame
		pygame.init()
		
		# load and set the logo & caption
		self.logopath = Path("assets/logo32x32.png")
		self.logo = pygame.image.load(self.logopath.resolve().as_posix())
		pygame.display.set_icon(self.logo)
		pygame.display.set_caption("ISP Game")
		
		# create a surface on the screen
		self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		
		# set background
		self.screen.fill((255,255,255))
	
		# create the player character
		self.playerChar = character.Player()
	
		# define how many pixels we move our character each frame
		self.step_x = 1
		self.step_y = 1
	
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self.running = False
		elif event.type == pygame.KEYDOWN:
			if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
				self.playerChar.run("right")
			elif (event.key == pygame.K_LEFT or event.key == pygame.K_a):
				self.playerChar.run("left")
			elif (event.key == pygame.K_UP or event.key == pygame.K_w):
				self.playerChar.jump()
		elif event.type == pygame.KEYUP:
			self.playerChar.stop()
	
	def on_loop(self):
		if (self.playerChar.getRun() == True):
			if (self.playerChar.getDirection() == "right"):
				if (self.playerChar.getX() < self.width-32):
					self.playerChar.move(1)
			elif (self.playerChar.getDirection() == "left"):
				if (self.playerChar.getX() > 0):
					self.playerChar.move(-1)
	
	def on_render(self):
		# clear the screen
		self.screen.fill((255,255,255))
		# draw the player character
		self.playerChar.draw(self.screen)
		# update the display
		pygame.display.flip()
	
	def on_cleanup(self):
		pygame.quit()
	
	def on_execute(self):
		if self.on_init() == False:
			self.running = False
		
		while (self.running):
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()
		
		self.on_cleanup()

# run the main function only if this module is executed as the main script
if __name__ == "__main__":
	theApp = App()
	theApp.on_execute()

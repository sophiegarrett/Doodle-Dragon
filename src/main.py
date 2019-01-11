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
		self.playerpath = Path("assets/character/character.gif")
		self.playerChar = character.Character(50, 50, self.playerpath)
	
		# define how many pixels we move our character each frame
		self.step_x = 1
		self.step_y = 1
	
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self.running = False
	
	def on_loop(self):
		# fetch character position
		self.xpos = self.playerChar.getX()
		self.ypos = self.playerChar.getY()
		
		# move the character
		# check if the character is still on screen, if not change direction
		if self.xpos > self.width-32 or self.xpos < 0:
			self.step_x = -self.step_x
		if self.ypos > self.height-32 or self.ypos < 0:
			self.step_y = -self.step_y
		
		# update the position of the character
		self.xpos += self.step_x
		self.ypos += self.step_y
		self.playerChar.update(self.xpos, self.ypos)
	
	def on_render(self):
		# draw the player character
		self.playerChar.draw(self.screen)
	
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

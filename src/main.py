# main module
import pygame
from pathlib import Path
import character
import level

# main class
class App:
	def __init__(self):
		self.running = True
		self.screen = None
		self.size = self.width, self.height = 1024, 576
		self.floor = 416
	
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
		
		# initialize level 1
		self.currentLevel = level.Level(1)
		self.currentLevel.display(self.screen)
	
		# create the player character
		self.playerChar = character.Player(self.floor)
	
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
			elif (event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE):
				if (self.playerChar.checkJump() == -1):
					self.playerChar.jump()
		elif event.type == pygame.KEYUP:
			if (pygame.key.get_pressed()[pygame.K_RIGHT] == False and pygame.key.get_pressed()[pygame.K_LEFT] == False
				and pygame.key.get_pressed()[pygame.K_a] == False and pygame.key.get_pressed()[pygame.K_d] == False):
				self.playerChar.stopX()
	
	def on_loop(self):
		if (self.playerChar.getXMomentum() == 1):
			if (self.playerChar.getX() < self.width-32):
				self.playerChar.moveX(2)
		elif (self.playerChar.getXMomentum() == -1):
			if (self.playerChar.getX() > 0):
				self.playerChar.moveX(-2)
		
		if (self.playerChar.getYMomentum() >= 1):
			if (self.playerChar.getY() > 0):
				self.playerChar.moveY(-1)
		elif (self.playerChar.getYMomentum() <= -1):
			if (self.playerChar.getY() < self.floor):
				self.playerChar.moveY(1)
		
		if (self.playerChar.checkJump() >= 21):
			self.playerChar.tickJump()
		elif (self.playerChar.checkJump() >= 1):
			self.playerChar.tickJump()
			self.playerChar.setYMomentum(0)
		elif (self.playerChar.checkJump() == 0):
			self.playerChar.setYMomentum(-1)
		
		if (self.playerChar.checkJump() == 0 and self.playerChar.getY() == self.floor):
			self.playerChar.stopJump()
	
	def on_render(self):
		# display the current level
		self.currentLevel.display(self.screen)
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

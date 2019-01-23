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
		pygame.display.set_caption("ISP Game - Doodle Dragon")
		
		# create a surface on the screen
		self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		
		# initialize level 1
		self.currentLevel = level.Level(1)
		self.currentLevel.display(self.screen)
		
		# initialize characters
		self.characters = pygame.sprite.Group()
		# create the player character
		self.playerChar = character.Player(self.floor)
		self.characters.add(self.playerChar)
	
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self.running = False
		elif event.type == pygame.KEYDOWN:
			if (event.key == pygame.K_RIGHT or event.key == pygame.K_d):
				self.playerChar.run(1)
			elif (event.key == pygame.K_LEFT or event.key == pygame.K_a):
				self.playerChar.run(-1)
			elif (event.key == pygame.K_UP or event.key == pygame.K_w or event.key == pygame.K_SPACE):
				if (self.playerChar.checkJump() == -1):
					self.playerChar.jump()
		elif event.type == pygame.KEYUP:
			if (pygame.key.get_pressed()[pygame.K_RIGHT] == False and pygame.key.get_pressed()[pygame.K_LEFT] == False
				and pygame.key.get_pressed()[pygame.K_a] == False and pygame.key.get_pressed()[pygame.K_d] == False):
				self.playerChar.stopX()
	
	def on_loop(self):
		# update all characters
		self.characters.update(self.width, self.height, self.floor)
	
	def on_render(self):
		# draw all characters on the screen
		self.characters.clear(self.screen, self.currentLevel.getBackground())
		self.characters.draw(self.screen)
		# update the display
		pygame.display.update()
	
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

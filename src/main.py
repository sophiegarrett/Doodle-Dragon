# main module
import pygame
import character

# define global variables
screen_width = 1024
screen_height = 576

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
		self.logo = pygame.image.load("logo32x32.png")
		pygame.display.set_icon(self.logo)
		pygame.display.set_caption("ISP Game")
		
		# create a surface on the screen
		self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		
		# set background
		self.screen.fill((255,255,255))
	
		# create the main character
		self.mainChar = character.Character(50, 50, "character.gif")
	
		# define how many pixels we move our character each frame
		self.step_x = 1
		self.step_y = 1
	
		# define a variable to control the main loop
		self.running = True
	
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self.running = False
	
	def on_loop(self):
		# fetch character position
		self.xpos = self.mainChar.getX()
		self.ypos = self.mainChar.getY()
		
		# move the character
		# check if the character is still on screen, if not change direction
		if self.xpos > self.width-32 or self.xpos < 0:
			self.step_x = -self.step_x
		if self.ypos > self.height-32 or self.ypos < 0:
			self.step_y = -self.step_y
		
		# update the position of the character
		self.xpos += self.step_x
		self.ypos += self.step_y
		self.mainChar.update(self.xpos, self.ypos)
	
	def on_render(self):
		# draw the main character
		self.mainChar.draw(self.screen)
	
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

# define a main function
def main():
	
	# initialize pygame
	pygame.init()
	
	# load and set the logo
	logo = pygame.image.load("logo32x32.png")
	pygame.display.set_icon(logo)
	pygame.display.set_caption("ISP Game")
	
	# create a surface on the screen
	global screen
	screen = pygame.display.set_mode((screen_width,screen_height))
	
	# set background
	screen.fill((255,255,255))
	
	# create the main character
	mainChar = character.Character(50, 50, "character.gif")
	
	# define how many pixels we move our character each frame
	step_x = 1
	step_y = 1
	
	# define a variable to control the main loop
	running = True
	
	# main loop
	while running:
		# fetch character position
		xpos = mainChar.getX()
		ypos = mainChar.getY()
		
		# move the character
		# check if the character is still on screen, if not change direction
		if xpos > screen_width-32 or xpos < 0:
			step_x = -step_x
		if ypos > screen_height-32 or ypos < 0:
			step_y = -step_y
		
		# update the position of the character
		xpos += step_x
		ypos += step_y
		mainChar.update(xpos, ypos)
		
		# now put the character on screen
		mainChar.draw(screen)
		
		# event handling, gets all events from the event queue
		for event in pygame.event.get():
			# only do something if the event is of type QUIT
			if event.type == pygame.QUIT:
				# change the value to False, to exit the main loop
				running = False

# run the main function only if this module is executed as the main script
if __name__ == "__main__":
	theApp = App()
	theApp.on_execute()
	# call the main function
	# main()

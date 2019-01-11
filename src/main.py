# main module
import pygame
import character

# define global variables
screen_width = 1024
screen_height = 576

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
	# call the main function
	main()

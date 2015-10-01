#imports
import pygame , sys
from constant import *
from loader import musicloader

def intro():
	pygame.init() #Initialized Pygame
	clock = pygame.time.Clock() #Initialize pygame clock which is used to control frames per second and bunch of different time realted things
	music = musicloader("invincible.ogg")#loads the music and is basically a call to the class musicloader in loader.py 
	music.play()#starts the music
	screen = pygame.display.set_mode((SCREENWIDTH , SCREENHEIGHT))#sets up the pygame screen , all the constant with capital letter are defined inside of constant.py
	running = True#Loop runner
	flag = 0
	background = pygame.Surface(screen.get_size())#gets size of the pygame surface
	background = background.convert()#converts background ,  which is faster for blitting sprites onto it
	background.fill(BLACK)#fills the background with BLACK COLOR and is defined inside of constant.py
	while running :
		for event in pygame.event.get():#checks for the interrupts raised by I/O devices 
			if event.type == pygame.QUIT :#checks if the cross button on the top of the window is hitted
				sys.exit()#exits everything
			elif event.type == pygame.KEYDOWN :#checks if the any key is pressed down
				if event.key == pygame.K_RETURN :#checks if enter button is hit
					running = False#stops the loop si that the program terminates and the game starts (look main.py)
				elif event.key == pygame.K_ESCAPE :#checks if escape button is hitted down
					sys.exit()
		font = pygame.font.Font(None, 96)#sets font size with None effect (Means just Normal Text)
		font2 = pygame.font.Font(None, 24)
		flag ^=1
		if flag :
			text = font.render("DONKEY-KONG" , 1, BLUE)#basically renders the word with BLUE color
		else:
			text = font.render("DONKEY-KONG" , 1, GREEN)
		text2 =  font2.render("PRESS ENTER TO START THE GAME" , 1, WHITE)
		#in both the textpos we have overriden the centerx and centery to make the text position beautiful and have exctracted background's width and height
		textpos2 = text.get_rect(centerx=background.get_width()/2 + 100, centery=background.get_height()/2 + 100)
		textpos = text.get_rect(centerx=background.get_width()/2 , centery=background.get_height()/2  - 50)
		screen.blit(text, textpos)#kind of attach/render it to screen
		screen.blit(text2,  textpos2)
		pygame.display.update()#Keep on updating the screen because it will be rendered everytime it will be run
		clock.tick(FPSLOW)#set's the frame per second to the variable FPSLOW  (look constant.py)
	music.stop()#stops the music (defined in musicloader class in loader.py file)

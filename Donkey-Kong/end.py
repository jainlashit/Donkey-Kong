import pygame , sys
from constant import *
from loader import musicloader

def end(score , board):
	level = board.getLevel()#gets level of player instance created in "board.py"
	life = board.player.life#gets life's of player instance created in "board.py"
	pygame.init()#Initialized Pygame
	clock = pygame.time.Clock()#Initialize pygame clock which is used to control frames per second and bunch of different time realted things
	music = musicloader("game_over.ogg")#loads the music and is basically a call to the class musicloader in loader.py 
	music.play()#starts the music
	screen = pygame.display.set_mode((SCREENWIDTH , SCREENHEIGHT))#sets up the pygame screen , all the constant with capital letter are defined inside of constant.py
	running = True#Loop runner
	background = pygame.Surface(screen.get_size())#gets size of the pygame surface
	background = background.convert()#converts background ,  which is faster for blitting sprites onto it
	background.fill(BLACK)#fills the background with BLACK COLOR and is defined inside of constant.py
	while running :
		for event in pygame.event.get():#checks for the interrupts raised by I/O devices 
			if event.type == pygame.QUIT :#checks if the cross button on the top of the window is hitted
				sys.exit()#exits everything
			elif event.type == pygame.KEYDOWN :#checks if the any key is pressed down
				if event.key == pygame.K_ESCAPE :#checks if escape button is pressed down
					sys.exit()
		font = pygame.font.Font(None, 48)#sets font size with None effect (Means just Normal Text)
		font2 = pygame.font.Font(None, 96)
		if level == 3 and life >0 :
			text2 = font2.render( "YOU WON ! " , 1, GREEN)#basically renders the word with GREEN color
		else :
			text2 = font2.render( "YOU LOST ! " , 1, RED)
		text = font.render( "You score: %s" %str(score), 1, BLUE )
		#in both the textpos we have overriden the centerx and centery to make the text position beautiful and have exctracted background's width and height
		textpos = text.get_rect(centerx=background.get_width()/2 -50 , centery=background.get_height()/2+50)
		textpos2 = text.get_rect(centerx=background.get_width()/2 -100 , centery=background.get_height()/2-50)
		screen.blit(text, textpos)#kind of attach/render it to screen
		screen.blit(text2 , textpos2)
		pygame.display.update()#Keep on updating the screen because it will be rendered everytime it will be run
		clock.tick(FPSLOW)#set's the frame per second to the variable FPSLOW  (look constant.py)
	music.stop()#stops the music (defined in musicloader class in loader.py file)
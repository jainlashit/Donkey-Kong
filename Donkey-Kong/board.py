import pygame,sys,random
from fire import fire
from spriteloader import Sprite
from monster import monster
from player import player
from loader import imageloader
from loader import musicloader
from loader import soundloader
from end import end
from constant import *
from level01 import level01
from level02 import level02

class board:

	def __init__(self , width , height ,level , life ,coins):
            pygame.init()#initialises pygame
            self.height = height	
            self.width = width
            self.screen = pygame.display.set_mode((self.width,self.height))#sets up display for pygame
            self.clock = pygame.time.Clock()#Initialize pygame clock which is used to control frames per second and bunch of different time realted things
            self.firelist = []#Contain all the sprites of fire
            self.running = 1 #loop running variable
            self.__level = level # private variable and sets it to current level 
            self.score = 0 #score of player
            self.theme_music = musicloader("main_theme.ogg")#loads in the music  from musicloader class of "loader.py"
            self.coin_sound = soundloader("coin.ogg")#loads in the coin taking sound from soundloader class of "loader.py"
            #difference between music and sound is that music is like game song and sound is like sound effects , only one music can be loaded and 
            #hence played at a time and at max eight sounds can be played together 
            self.theme_music.play()#playes in the music
            self.play(life , coins)#calls play function
            if self.__level <=2 and self.player.life:#if life is > 0 and level is less or equal to 2
                start(self.__level , self.player.life , self.player.coins)
            self.theme_music.stop()#stops the music
            end(self.score , self)#calls in end function from "end.py"

        def getLevel(self):#getX function used for encapsulation 
            return self.__level

        def setLevel(self,levela):#setX function for encapsulation
            self.__level = levela
            return

	def play(self , life , coins):
            self.loadsprite()# call loadsprite method below
            self.player.coins = coins#sets coins if level upgraded or player dies
            self.player.alive = True#checks if player is alive 
            self.player.life = life#loads number of lives left for player
            self.background = pygame.Surface(self.screen.get_size())
            self.background = self.background.convert()
            self.background.fill(BLACK)#fills screen with black color
            self.brick_sprites.draw(self.background)#draws brick sprites onto screen
            while self.running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT :
                        sys.exit()
                    elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                        if event.key == pygame.K_ESCAPE :
                            sys.exit()
                        self.player.move(event)#if button is pressed it calls move method in player class if it was supposed to move
                for fire_sprites in self.firelist :#POLYMORPHISM below , overrides update method of pygame.sprite.Sprite
                    self.player_sprites.update(self.brick_sprites , self.ladder_sprites , self.tank_sprites , fire_sprites, self.monster_sprites)
                for fire_sprites in self.firelist :
                    fire_sprites.update(self.ladder_sprites,self.brick_sprites)
                for fire_sprites in self.firelist :
                    pygame.sprite.spritecollide(self.tank,fire_sprites,True)#checks if tank sprites with a radioactive sign collides with fire sprites and True makes the fire disappear 
                lstCols = pygame.sprite.spritecollide(self.player, self.coin_sprites, True)#adds all collision of coin and player , TRUE means that coin will disappear after collision
                if len(lstCols) == 1:
                    self.player.coins = self.player.coins + len(lstCols)
                    self.coin_sound.play()
                self.monster.move()
                self.score = 5*self.player.coins
                self.screen.blit(self.background, (0, 0)) 
                font = pygame.font.Font(None, 36)
                text = font.render("Score : %s" % self.score , 1, (255, 0, 0))
                textpos = text.get_rect(centerx=self.background.get_width()/2 + 200)
                text1 = font.render("Life Left : %s" % self.player.life , 1, (255, 0, 0))
                textpos1 = text.get_rect(centerx=self.background.get_width()/2 + 400)
                self.screen.blit(text, textpos)
                self.screen.blit(text1, textpos1)
                if not self.player.alive:
                    self.running  = 0
                if pygame.sprite.spritecollide(self.player,self.queen_sprites,False):
                    self.__level+=1
                    self.running = 0
                #below , we've added rendered all the sprites onto our screen
                self.brokenladder_sprites.draw(self.screen)
                self.coin_sprites.draw(self.screen)
                self.ladder_sprites.draw(self.screen)
                self.player_sprites.draw(self.screen)
                self.tank_sprites.draw(self.screen)
                self.queen_sprites.draw(self.screen)
                self.monster_sprites.draw(self.screen)
                for fire_sprites in self.firelist :
                    fire_sprites.draw(self.screen)
                #generates fire randomly
                if random.randint(0,FIREFREQ)==FIREVALUE:
                    self.generatefire()
                self.clock.tick(FPS)
                pygame.display.update()
                
	def loadsprite(self):
	    x_offset = (BRICKSIZE/2)
            y_offset = (BRICKSIZE/2)
            if self.__level == 1 :
                level = level01()
                layout = level.getLayout()
                img_list = level.getSprites()
            elif self.__level ==2 :
                level = level02()
                layout = level.getLayout()
                img_list = level.getSprites()  
            self.brick_sprites = pygame.sprite.Group()
            self.coin_sprites = pygame.sprite.Group()
            self.ladder_sprites = pygame.sprite.Group()
            self.brokenladder_sprites = pygame.sprite.Group()
            for y in xrange(len(layout)):
                for x in xrange(len(layout[y])):
                    centerPoint = [(x*BRICKSIZE)+x_offset,(y*BRICKSIZE+y_offset)]#calculated centerpoint becoz we have to place the center exactly on the position of matrix
                    if layout[y][x]==level.BRICK:
                        brick = Sprite(centerPoint, img_list[level.BRICK])
                        self.brick_sprites.add(brick)
                    elif layout[y][x]==level.PLAYER:
                        self.player = player(centerPoint,img_list[level.PLAYER])
                    elif layout[y][x]==level.COIN:
                        coin = Sprite(centerPoint, img_list[level.COIN])
                        self.coin_sprites.add(coin)
                    elif layout[y][x]==level.LEFT_LADDER :
                        ladder = Sprite(centerPoint , img_list[level.LEFT_LADDER])
                        self.ladder_sprites.add(ladder) 
                    elif layout[y][x]==level.RIGHT_LADDER :
                        ladder = Sprite(centerPoint , img_list[level.RIGHT_LADDER])
                        self.ladder_sprites.add(ladder)
                    elif layout[y][x] == level.TANK:
                        self.tank = Sprite(centerPoint,img_list[level.TANK])
                    elif layout[y][x] == level.MONSTER :
                        self.monster = monster(centerPoint,img_list[level.MONSTER])
                    elif layout[y][x] == level.FIRE :
                        self.fire = fire(centerPoint,img_list[level.FIRE])
                    elif layout[y][x] == level.QUEEN :
                        self.queen = Sprite(centerPoint , img_list[level.QUEEN])
                    elif layout[y][x] == level.BROKENLADDERLEFT :
                        self.broke = Sprite(centerPoint , img_list[level.BROKENLADDERLEFT])
                        self.brokenladder_sprites.add(self.broke)
                    elif layout[y][x] == level.BROKENLADDERRIGHT :
                        self.broke = Sprite(centerPoint , img_list[level.BROKENLADDERRIGHT])
                        self.brokenladder_sprites.add(self.broke)
            self.player_sprites = pygame.sprite.RenderPlain(self.player)
            self.monster_sprites = pygame.sprite.RenderPlain(self.monster)    
            self.firelist.append(pygame.sprite.RenderPlain(self.fire))   
            self.tank_sprites = pygame.sprite.RenderPlain(self.tank)
            self.queen_sprites = pygame.sprite.RenderPlain(self.queen)
        
        def generatefire(self):
            if self.__level==1:
                level = level01()
                layout = level.getLayout()
                img_list = level.getSprites()
            elif self.__level ==2 :
                level = level02()
                layout = level.getLayout()
                img_list = level.getSprites()
            centerPoint = [108,180]
            self.fire = fire(centerPoint,img_list[level.FIRE])
            self.firelist.append(pygame.sprite.RenderPlain(self.fire))
            
def start(level , life ,coins):
    #creates instance of this file
    begin = board(SCREENWIDTH, SCREENHEIGHT, level, life , coins)

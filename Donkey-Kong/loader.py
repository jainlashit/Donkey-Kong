import os, sys
import pygame
from pygame.locals import *

if not pygame.image : print 'Warning , image disabled'
if not pygame.font : print 'Warning , fonts disabled'
if not pygame.mixer : print 'Warning , sound disabled' 
if not pygame.font : print 'Warning , fonts disabled'

def imageloader(name, colorkey=None):
    fullname = os.path.join('data', 'images')#joins "data" and "images" by operating system divider like "/" for linux and "\" windows
    fullname = os.path.join(fullname, name)
    try:
        image = pygame.image.load(fullname)#loads image if in loadable format
    except pygame.error, message:#throws an error if image is not in loadble format
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()#converts image in such a form which is easy for blitting on surface
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)#makes the background colorless
    return image, image.get_rect()

class musicloader():
    def __init__(self , name):
        temp = os.path.join('data' , 'music')
        self.path = os.path.join(temp , name)
        self.music  = pygame.mixer.music #initialises music 
        self.music.load(self.path)#loads music

    def play(self): 
        self.music.play(-1 , 0.0)#plays music

    def stop(self):
        self.music.stop()#stops music

class soundloader():
    def __init__(self , name):
        temp = os.path.join('data' , 'sound')
        self.path = os.path.join(temp , name)
        self.sound = pygame.mixer.Sound(self.path)#initialises sound element
    def play(self):
        self.sound.play()#plays the initialised sound

    def stop(self):
        self.sound.stop()#stop the initialised sound
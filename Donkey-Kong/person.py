import pygame , sys
from constant import *
from loader import imageloader
from spriteloader import Sprite

class person(Sprite):
    def __init__(self, centerPoint, image): 
        Sprite.__init__(self, centerPoint, image)
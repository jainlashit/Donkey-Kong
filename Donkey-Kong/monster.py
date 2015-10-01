import pygame
from person import person
from constant import *

class monster(person):

    def __init__(self, centerPoint, image):
        person.__init__(self , centerPoint, image) 
        self.dx = 0
        self.flag = 0

    def move(self):

    	self.dx+=1
    	if self.dx == 100:
    		self.dx = 0
    		self.flag ^=1
    	if self.flag :
    		self.rect.move_ip((-1,0))
    	else:
    		self.rect.move_ip((1,0))

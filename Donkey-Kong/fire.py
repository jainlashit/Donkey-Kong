import pygame , sys , random
from constant import *
from loader import imageloader
from spriteloader import Sprite

class fire(Sprite):
    def __init__(self, centerPoint, image):
        Sprite.__init__(self, centerPoint , image)
        self.dx = 2
        self.dy = 2
        self.collide  = False

    def update(self, ladder_group , brick_group):
    	self.rect.move_ip(0 , self.dy)
        if pygame.sprite.spritecollide(self, brick_group, False) and not self.collide:
        	self.rect.move_ip(0 , -1*self.dy)
                self.rect.move_ip(self.dx , 0)
                if pygame.sprite.spritecollide(self, brick_group, False):
                    self.dx *= -1
                self.collide = False
        else :
            if pygame.sprite.spritecollide(self, ladder_group, False):
                temp = random.randint(0,1)
                if temp or self.collide :
                    self.collide = True
                    if pygame.sprite.spritecollide(self, brick_group, False):
                        self.collide = False
                if not self.collide:
                    self.rect.move_ip(0 , -1*self.dy)
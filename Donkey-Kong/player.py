import pygame
from person import person
from constant import *
from loader import soundloader

class player(person):

    def __init__(self, centerPoint, image):
        person.__init__(self , centerPoint, image) 
        self.life = 3
        self.alive = True
        self.coins = 0
        self.dx = 0
        self.dy = 0
        self.climb = 0#decides if player will climb ladder or not
        self.jump = 0#decides if player will jump or not
        self.jumpd = -1#decides whether to move up down/up
        self.jumpl = 0#saves jump length
        self.yspeed = PLAYERSPEED
        self.xspeed = PLAYERSPEED
        self.jump_sound = soundloader("jump.ogg")

    def move(self , event):
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_w :#w key
                if self.climb:
                    self.dy -= self.yspeed
            elif event.key == pygame.K_s :#s key
                self.dy += self.yspeed
            elif event.key == pygame.K_d :#d key
                self.dx += self.xspeed
            elif event.key == pygame.K_a :#a key
                self.dx -= self.xspeed
            elif event.key == pygame.K_SPACE:#space key
                if not self.jump:
                    self.jump_sound.play()
                    self.jump=1
                    self.jumpd=-1
        else:
            if event.key == pygame.K_w :
                self.dy = 0
            elif event.key == pygame.K_s :
                self.dy = 0
            elif event.key == pygame.K_d :
                self.dx = 0
            elif event.key == pygame.K_a :
                self.dx = 0 

    def update(self , brick_group , ladder_group , tank_group , fire_group , monster_group):
        if pygame.sprite.spritecollide(self, ladder_group, False) and not self.jump:
            self.climb = 1
        else:
            self.climb = 0
        if self.jump:
            self.dy = self.jumpd
            self.jumpl -= self.jumpd
            if self.jumpl >= JUMPLIMIT :
                self.jumpd = 1
                self.jumpl = JUMPLIMIT
            if self.jumpl == 0:
                self.jump = 0
                self.dy = 0
        self.rect.move_ip(self.dx , self.dy)
        if pygame.sprite.spritecollide(self, brick_group, False) or pygame.sprite.spritecollide(self, tank_group , False):
            self.rect.move_ip(-self.dx,-self.dy)
        if pygame.sprite.spritecollide(self , fire_group , True) or pygame.sprite.spritecollide(self , monster_group , False):
            self.life-=1
            self.alive = False
            self.coins-=5
        self.in_air(brick_group , ladder_group)

    def in_air(self , brick_group , ladder_group):
        #is an implementation for gravity if person is hanging in air
        self.rect.move_ip(0 , 1)
        if not pygame.sprite.spritecollide(self , brick_group , False) and not self.jump and not self.climb and not pygame.sprite.spritecollide(self , ladder_group , False):
            self.jump = 1
            self.jumpl = JUMPLIMIT + 1
        if pygame.sprite.spritecollide(self , ladder_group , False) and self.jump:
            self.jumpl = self.jumpd
        self.rect.move_ip(0 , -1)

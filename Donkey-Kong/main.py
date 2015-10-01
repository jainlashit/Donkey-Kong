import pygame
from intro import intro
from board import start
from board import board

if __name__ == "__main__":#whenever you run this file by actually running it ;)
	intro()#calls into from intro .py
	score = start(1 , 3, 0)	#start level1 from board.py start(level_number , life_given , initial_coins)

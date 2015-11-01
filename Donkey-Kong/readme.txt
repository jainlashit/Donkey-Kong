Hey! , Welcome to Donkey-Kong 
This assignment is submittged by Lashit Jain (201402162) .

For Gamers :
This a two level game and we have to save our queen twice . Once the queen is reached , we move onto next level .To start playing just run the following commmand " python main.py "

Controls :
	 A -> Left 
	 D -> Right
	 S -> Climb Down (On Ladder)
	 W -> Climb Up (On Ladder)
	 Space -> Jump(Disabled while climbing ladder)

For Coders:
	Well the most absurd thing I've added to project is my "constant.py" file , which stores all the static variable . So if you find any variables with CAPITAL LETTERS and think where the hell have they come from just look up for "constant.py" file :)
	I've tried to keep file name and class name the same(in case there is only one class inside of file)

For Graders(My Dear TA's) :
	Following classes have been implemented as per your wish
	1 PERSON in person.py
	2 PLAYER in player.py
	3 DONKEY(MONSTER FOR ME) in monster.py
	4 BOARD in board.py
	5 FIRE in fire.py

	OOP's concepts :
		INHERITANCE :
			1 Player and Monster inherit from Person
			2 Person even inherits from Sprite in from spriteloader.py
			3 Sprites inturn inherits from pygame.sprite.Sprite
			4 level01 and level02 have inherited from level
			5 and there are a bunch of more classes which inherits 
		POLYMORPHISM :
			checkout person player sprite and monster __init__ and update in case of person & sprite
			1	Line 62 of board.py self.player_sprites.update(self.brick_sprites , self.ladder_sprites , self.tank_sprites , fire_sprites, self.monster_sprites)
				I've modified update funciton of pygame.sprite.Sprite and used it to detect sprite collision
				Similarly for line 64
			2 and many more 
		ENCAPSULATION :
			Look board.py line number 35 and 38 and I've extracted the data inside of "end.py"
		MODULARITY :
			Everywhere except this file ;) 

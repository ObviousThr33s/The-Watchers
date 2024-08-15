import os
import time


import gameInput
import board
import game

#defines the size of the board
X = 80
Y = 40

#defines the game components 
#currently there is only the map and the commands
#to-do: dungeon crawler style renderer
c = gameInput.gameInput
b = board.Board
g = game.Game


def __init__():
	c.__init__(c)
	b.__init__(b, X, Y)
	g.__init__(g,b)

def __main__():
	
	#flow determines the component in use
	#much like a switch statement
	flow = 0
	ticks = 0

	while True:
		#clears the screen after each draw
		#platform specific, windows only right now
		os.system("cls")

		#initially flow goes to the board state
		if flow == 0:
			#updates the board
			b.update(b)
			#prints the board
			b.printBoard(b)
			
			#completes game tasks to be updated next tick
			g.update(g, ticks)

			#determines test task order
			ticks+=1
			#moves to next flow state
			flow += 1
		
		if flow == 1:
			#calls the command system
			c.cs(c)
			#gives a short rest for program to catch up if needed
			time.sleep(.05)
			flow = 0


__init__()
__main__()
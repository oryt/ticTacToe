#!/usr/bin/env python
# TicTacToe 
# Thanks to Christian Thompson for idea on graphics and core game mechanics  
#Please run in full screen

# load the modules needed, os to enable use of clear and time to use sleep
import os
import time


# The Board
TreiRad = ["", " ", " ", " ", " ", " ", " ", " ", " ", " "]

#welcome and instructions
def welcome():

	print"""
 .-') _   _  .-')     ('-.                           _  .-')     ('-.     _ .-') _   
(  OO) ) ( \( -O )  _(  OO)                         ( \( -O )   ( OO ).-.( (  OO) )  
/     '._ ,------. (,------.         ,-.-')          ,------.   / . --. / \     .'_  
|'--...__)|   /`. ' |  .---'  .-')   |  |OO)   .-')  |   /`. '  | \-.  \  ,`'--..._) 
'--.  .--'|  /  | | |  |    _(  OO)  |  |  \ _(  OO) |  /  | |.-'-'  |  | |  |  \  ' 
   |  |   |  |_.' |(|  '--.(,------. |  |(_/(,------.|  |_.' | \| |_.'  | |  |   ' | 
   |  |   |  .  '.' |  .--' '------',|  |_.' '------'|  .  '.'  |  .-.  | |  |   / : 
   |  |   |  |\  \  |  `---.       (_|  |            |  |\  \   |  | |  | |  '--'  / 
   `--'   `--' '--' `------'         `--'            `--' '--'  `--' `--' `-------'  

Time to play some tic-tac-toe or as its called in swedish tre i rad
To place your choiche please enter a number between 1 to 9.

"""
os.system("clear")
welcome ()

# Ask the users to enter name
PlayerA = raw_input("Please enter name for player A ")
PlayerB = raw_input("Please enter name for player B ")
os.system("clear")

#function to print the board
def PrintBoard():
	print "   |   |   "
	print " "+TreiRad[1]+" | "+TreiRad[2]+" | "+TreiRad[3]+" "
	print "   |   |   "
	print "___|___|___"
	print "   |   |   "
	print " "+TreiRad[4]+" | "+TreiRad[5]+" | "+TreiRad[6]+" "
	print "   |   |   "
	print "___|___|___"
	print "   |   |   "
	print " "+TreiRad[7]+" | "+TreiRad[8]+" | "+TreiRad[9]+" "
	print "   |   |   "

# The main loop that keeps the game running unless win or draw
while True:
	os.system("clear")
	welcome ()
	PrintBoard()

	# asks Player A to please make his move
	# To check so the space is empty and if not tell user to pick another space
	# done with loop so unless the space is empty it will keep asking  	

	while True:

		print PlayerA 		
		YourMove = raw_input("Please make your move 1-9 ")
		YourMove = int(YourMove)
		if TreiRad[YourMove] == " ":  
			TreiRad[YourMove] = "X"
			break
		print"Please choose an empty space"
	time.sleep(2)


	
	# check if there is a winner and if so prints players name and then breaks main game loop.

	if (TreiRad[1] == "X" and TreiRad[2] == "X" and TreiRad[3] == "X") or \
		(TreiRad[4] == "X" and TreiRad[5] =="X" and TreiRad[6] == "X") or \
	 	(TreiRad[7] == "X" and TreiRad[8] =="X" and TreiRad[9] == "X") or \
	 	(TreiRad[1] == "X" and TreiRad[4] =="X" and TreiRad[7] == "X") or \
	 	(TreiRad[2] == "X" and TreiRad[5] =="X" and TreiRad[8] == "X") or \
	 	(TreiRad[3] == "X" and TreiRad[6] =="X" and TreiRad[9] == "X") or \
	 	(TreiRad[1] == "X" and TreiRad[5] =="X" and TreiRad[9] == "X") or \
	 	(TreiRad[3] == "X" and TreiRad[5] =="X" and TreiRad[7] == "X"):	
		os.system("clear")
		welcome ()
		PrintBoard()
		print "And we have a winner congratulations", PlayerA, "or Grattis as we say in Sweden"
		break
		
	os.system("clear")
	welcome ()
	PrintBoard()

	# Cheks for empty spaces on the board, if no empty space found then prints draw and breaks game main loop. 
	NoWinner = True
	for index in range(1, 10):
		if TreiRad[index] == " ":
			NoWinner = False
			break

	if NoWinner == True:
		print 'Draw'
		time.sleep(3)
		break

	# asks Player B to please make his move
	# To check so the space is empty and if not tell user to pick another space
	# done with loop so unless the space is empty it will keep asking   	

	while True:
		print PlayerB
		YourMove = raw_input("Please  make your move 1-9 ")
		YourMove = int(YourMove)

	  
		if TreiRad[YourMove] == " ":
			TreiRad[YourMove] = "O"
			break
	
	 	print"Please choose an empty space"
	time.sleep(2)

	# check if there is a winner and if so prints players name and then breaks main game loop.
	if (TreiRad[1] == "O" and TreiRad[2] =="O" and TreiRad[3] == "O") or \
		(TreiRad[4] == "O" and TreiRad[5] =="O" and TreiRad[6] == "O") or \
		(TreiRad[7] == "O" and TreiRad[8] =="O" and TreiRad[9] == "O") or \
		(TreiRad[1] == "O" and TreiRad[4] =="O" and TreiRad[7] == "O") or \
		(TreiRad[2] == "O" and TreiRad[5] =="O" and TreiRad[8] == "O") or \
		(TreiRad[3] == "O" and TreiRad[6] =="O" and TreiRad[9] == "O") or \
		(TreiRad[1] == "O" and TreiRad[5] =="O" and TreiRad[9] == "O") or \
		(TreiRad[3] == "O" and TreiRad[5] =="O" and TreiRad[7] == "O"):
		os.system("clear")
		welcome ()
		PrintBoard()
		print "And we have a winner congratulations", PlayerB, "or Grattis as we say in Sweden"
		break


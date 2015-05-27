#!/bin/python
# For problem statement see:
# https://projecteuler.net/problem=54
#Let's first empty the contents of hands.txt into an array
from pokerfunc import *
numlist = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
with open('hands.txt','r') as f:
	Rounds = [line.strip() for line in f]
for i in range (0, len(Rounds)):
	Rounds[i]= Rounds[i].split()
for i in range (0, len(Rounds)):
	for j in range (0,10):
		if list(Rounds[i][j])[0] == "T" :
			a = list(Rounds[i][j])
			a[0] = "10"
			Rounds[i][j] = a[0] + a[1]
		if list(Rounds[i][j])[0] == "J" :
                        a = list(Rounds[i][j])
                        a[0] = "11"
                        Rounds[i][j] = a[0] + a[1]
		if list(Rounds[i][j])[0] == "Q" :
                        a = list(Rounds[i][j])
                        a[0] = "12"
                        Rounds[i][j] = a[0] + a[1]
		if list(Rounds[i][j])[0] == "K" :
                        a = list(Rounds[i][j])
                        a[0] = "13"
                        Rounds[i][j] = a[0] + a[1]
		if list(Rounds[i][j])[0] == "A" :
                        a = list(Rounds[i][j])
                        a[0] = "14"
                        Rounds[i][j] = a[0] + a[1]
# The first 5 cards in each line are player ones, the second 5 are player 2's
# Let's split into two arrays for player 1 and player 2
Player1hands=[]
Player2hands=[]
for i in range (0,len(Rounds)):
	Player1hands.append(Rounds[i][:5])
	Player2hands.append(Rounds[i][5:])
# We now have 2 separate arrays for each player containing all of their hands
#Let's now check what elements are in each person's hand

Player1elems = [[0 for x in range(0,8)] for y in range(0,1000)] #arrays that will eventually contain ispair, isflush, etc.
Player2elems = [[0 for x in range(0,8)] for y in range(0,1000)]
for i in range (0,1000):
	Player1elems[i][0] = ispair(Player1hands[i])
	Player1elems[i][1] = istwopair(Player1hands[i])
	Player1elems[i][2] = isthreekind(Player1hands[i])
	Player1elems[i][3] = isfullhouse(Player1hands[i])
	Player1elems[i][4] = isstraight(Player1hands[i])
	Player1elems[i][5] = isflush(Player1hands[i])
	Player1elems[i][6] = isfourkind(Player1hands[i])
	Player1elems[i][7] = isstraightflush(Player1hands[i])
	Player2elems[i][0] = ispair(Player2hands[i])
        Player2elems[i][1] = istwopair(Player2hands[i])
        Player2elems[i][2] = isthreekind(Player2hands[i])
        Player2elems[i][3] = isfullhouse(Player2hands[i])
        Player2elems[i][4] = isstraight(Player2hands[i])
        Player2elems[i][5] = isflush(Player2hands[i])
        Player2elems[i][6] = isfourkind(Player2hands[i])
        Player2elems[i][7] = isstraightflush(Player2hands[i]) 

#Let's create a table that ranks hands from worst to best with numbers
#The higher the number, the better the hand
Player1handscore = [0 for x in range(1000)]
Player2handscore = [0 for x in range(1000)]

for i in range(0,1000):
		if "isstraightflush" in Player1elems[i]:
			Player1handscore[i] = "8"
		elif "isfourkind" in Player1elems[i]:
			Player1handscore[i] = "7"
		elif "isflush"  in Player1elems[i]:
			Player1handscore[i] = "6"
		elif "isstraight" in Player1elems[i]:
			Player1handscore[i] = "5"
		elif "isfullhouse" in Player1elems[i]:
			Player1handscore[i] = "4"
		elif "isthreekind" in Player1elems[i]:
			Player1handscore[i] = "3"
		elif "istwopair" in Player1elems[i]:
			Player1handscore[i] = "2"
		elif "ispair" in Player1elems[i]:
			Playerhandscore[i] = "1"

for i in range(0,1000):
     		if "isstraightflush" in Player2elems[i]:
        	        Player2handscore[i] = "8"
    	  	elif "isfourkind" in Player1elems[i]:
        	        Player2handscore[i] = "7"
       		elif "isflush" in Player2elems[i]:
        	        Player2handscore[i] = "6"
    	   	elif "isstraight" in Player2elems[i]:
       	        	Player2handscore[i] = "5"
        	elif "isfullhouse" in Player2elems[i]:
                	Player2handscore[i] = "4"
        	elif "isthreekind" in Player2elems[i]:
        	        Player2handscore[i] = "3"
        	elif "istwopair" in Player2elems[i]:
               		Player2handscore[i] = "2"
        	elif "ispair" in Player2elems[i]:
                	Player2handscore[i] = "1"

Scoresheet = [0 for x in range(1000)]

for i in range(0,1000):
	if Player1handscore[i] > Player2handscore[i]:
		Scoresheet[i] = "Player 1 wins"
	elif Player1handscore[i] < Player2handscore[i]:
		Scoresheet[i] = "Player 2 wins"
	elif Player1handscore[i] == Player2handscore[i]: #High card situation
		tmpp1 = []
		tmpp2 = []
		for j in range(0,5):
			tmpp1.append(list(Player1hands[i][j])[0]) #Separates 8D into 8,D then takes 8
			tmpp2.append(list(Player2hands[i][j])[0])	
		if max(tmpp1) > max(tmpp2):
			Scoresheet[i] = "Player 1 wins"
		elif max(tmpp1) < max(tmpp2):
			Scoresheet[i] = "Player 2 wins"
		else :
			Scoresheet[i] = "It's a tie"

#Let's now figure out who won and how many times

player1wincounter = 0
player2wincounter = 0
for i in Scoresheet:
	if i == "Player 1 wins":
		player1wincounter += 1
	elif i == "Player 2 wins":
		player2wincounter += 1
	else:
		continue

print "Player 1 won %d times" % (player1wincounter)
print "Player 2 won %d times" % (player2wincounter)
numties = 1000 - player1wincounter - player2wincounter
print "It was a tie %d times" % (numties)
#end of file		

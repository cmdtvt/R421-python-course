'''
The second exercise in this chapter continues with random selection. In this exercise the objective is to develop a game called nuke-foot-cockroach, which is pretty similar to the more popular variant, paper-rock-scissors. The rules are simple: both players select either nuke, foot or cockroach, and the winner is determined in the following way: Foot beats cockroach, nuke beats foot and cockroach beats nuke. If both the player and the AI select the same, it's a tie, except if both choose nuke, then both lose.


Implement the game so that the other player is computer controlled, and chooses randomly either foot(number 1), cockroach(number 3) or nuke(number 2). Also implement a feature which keeps the score, calculating both rounds the player won, and ties. If the player wins, print "You WIN!", if they loose "You LOSE!". If the round was a tie, either "It is a tie!" or "Both LOSE!", depending on if the tie was caused by a nuke or not. If the player selects "quit", the game ends and the final score is given. When the game works correctly, it prints the following:


########################
>>> 
Foot, Nuke or Cockroach? (Quit ends): Nuke
You chose: Nuke
Computer chose: Foot
You WIN!
Foot, Nuke or Cockroach? (Quit ends): Nuke
You chose: Nuke
Computer chose: Nuke
Both LOSE!
Foot, Nuke or Cockroach? (Quit ends): Cockroach
You chose: Cockroach
Computer chose: Nuke
You WIN!
Foot, Nuke or Cockroach? (Quit ends): Foot
You chose: Foot
Computer chose: Nuke
You LOSE!
Foot, Nuke or Cockroach? (Quit ends): Spaceshuttle
Incorrect selection.
Foot, Nuke or Cockroach? (Quit ends): Foot
You chose: Foot
Computer chose: Nuke
You LOSE!
Foot, Nuke or Cockroach? (Quit ends): Quit
You played 5 rounds, and won 2 rounds, playing tie in 0 rounds.
>>>  
########################	

Example output:
########################
Foot, Nuke or Cockroach? (Quit ends): Foot
You chose: Foot
Computer chose: Nuke
You LOSE!
Foot, Nuke or Cockroach? (Quit ends): Spaceshuttle
Incorrect selection.
Foot, Nuke or Cockroach? (Quit ends): Cockroach
You chose: Cockroach
Computer chose: Nuke
You WIN!
Foot, Nuke or Cockroach? (Quit ends): Cockroach
You chose: Cockroach
Computer chose: Nuke
You WIN!
Foot, Nuke or Cockroach? (Quit ends): Quit
You played 3 rounds, and won 2 rounds, playing tie in 0 rounds.
########################
'''


import random

wins = 0
loses = 0
rounds = 0
selections = ['Nuke','Foot','Cockroach']

def checkWins(f,s):
    pass

while True:
    s = input("Foot, Nuke or Cockroach? (Quit ends): ")
    if s == "quit":
        break
    elif s == "Foot":
        s = 1
    elif s == "Nuke":
        s = 2
    elif s == "Cockroach":
        s = 3

    c = random.randrange(1,2)
    print("You chose: "+str(s))
    print("Computer chose: "+str(selections[c+1]))

    if s == 3 and c == 3:
        print("Both lose")
    elif s == c:
        print("Its a tie!")

    elif s > c or s == 3 and c == 1:
        print("Player wins")
    else:
        print("Player lost")
 

    

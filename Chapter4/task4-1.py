'''
The first exercise in the fourth chapter is a basic while-iteration. The assignment is simple: create a program which on each turn prints the round number. Start by the round number 0 and make the iteration continue for four loops. When the program works correctly, it prints out something like this:



################
This is lap 0
This is lap 1
This is lap 2
This is lap 3
This is lap 4
################


The best way to approach this is probably by making two variables. The first one has the current lap number, and the other one marks the point where the iteration is stopped.

################
Example output:
This is lap 0
This is lap 1
This is lap 2
This is lap 3
This is lap 4
################
'''

l = 0
while True:
    print("This is lap "+str(l))
    if l == 4:
        break
    l += 1
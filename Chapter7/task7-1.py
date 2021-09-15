'''
The first exercise in this chapter consists of simple module library operations. In the chapter, a module called random was introduced. This module consists of several functions which can be used to get random numbers. The idea here is to create a program, which simulates coin flips by randomly selecting 0 (Tails) or 1 (Heads) and printing out the result. When working correctly, the program prints out something like this:


#############################
>>> 
Heads!
#############################

Obviously, as the program applies random activities, it may give any combination of five heads or tails. For example, running the program a second time resulted in this:

#############################
5 coin flips:
Tails!
Heads!
Heads!
Tails!
Heads!
>>> 
#############################


Example output:
#############################
Tails!
#############################
'''


import random
am = 5#int(input())
print(str(am)+" coin flips: ")
for i in range(am):
    if random.randrange(0,2) == 0:
        print("Tails!")
    else:
        print("Head!")
        
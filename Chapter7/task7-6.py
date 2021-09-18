'''
The last exercise in this chapter adds a small feature to the other continuous exercise project, the notebook. In this exercise, add a feature which includes the date and time of the written note to the program. The program works as earlier, but saves data in the form "[note]:::[date and time]" meaning that there is a three-colon separator between the note and timestamp. The timestamp can be generated as follows:

#######################	
>>> import time		

>>> time.strftime("%X %x")
'19:01:34 01/03/09'
>>> 
#######################	


This returns the date and time in a nice, compact string. When working correctly, the program prints the following:

#######################			
>>> 
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 2
Write a new note: Call mom.
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 1
Call mom.:::11:44:41 04/25/11

(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 4
Notebook shutting down, thank you.
>>> 
#######################	

Example output:
#######################	
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 2
Write a new note: Play football
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 1
Play football:::21:11:24 11/04/11

(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 4
Notebook shutting down, thank you.
#######################	
'''

import time
notes = []
#f = open("notebook.txt","r")
#notes = f.readlines()
#f.close()

while True:
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Empty the notebook")
    print("(4) Quit")

    select = input("Please select one: ")
    select = int(select)
    if select == 1:
        temp = ""
        for i in notes:
            temp += i+"\n"
        print(temp)

    elif select == 2:
        note = input("Write a new note: ")
        notes.append(note+":::"+time.strftime("%X %x"))
    elif select == 3:
        notes = []
        print("Notes deleted.")
    elif select == 4:
        f = open("notebook.txt", "w")
        for i in notes:
            f.write(i+"\n")
        f.close()
        print("Notebook shutting down, thank you.")
        break
'''
The last exercise in this chapter is the first part of the second multi-part assignment of this course, the notebook. In this notebook the user is able to add, read and delete notes from a separate note file "notebook.txt".


Create a program which allows the user to
(1) Read the contents of the notebook
(2) Add notes to the file or
(3) Delete all of the notes.
If the user selects 1, the entire notebook file is printed to the screen, if 2 then the program prompts "Write a new note: ", and adds the written note as the last line into the file with a trailing line break "\n". If the player selects 3, the file is emptied and the message "Notes deleted" will be shown. Also add the option (4) Quit, which ends the program, printing "Notebook shutting down, thank you.". With other selections the program prompts "Incorrect selection". When working, the program prints following:

##############
>>> 
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 2
Write a new note: Buy new tires
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 2
Write a new note: Buy new headlights
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 1
Buy new tires
Buy new headlights

(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 3
Notes deleted.
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 4
Notebook shutting down, thank you.
>>>
##############

Notice that the fastest way to delete a file's contents is to open it with mode "w" and close it immediately.


Example output:
##############
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 1
Buy milk

(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 2
Write a new note: Buy car
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 1
Buy milk
Buy car

(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 4
Notebook shutting down, thank you.
##############
'''

notes = []
f = open("notebook.txt","r")
notes = f.readlines()
f.close()

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
        notes.append(note)
    elif select == 3:
        notes = []
        print("Notes deleted.")
    elif select == 4:
        print("Notebook shutting down, thank you.")
        break

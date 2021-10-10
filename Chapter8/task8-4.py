'''

'''

import time
notes = []
notebook = "notebook.txt"


def save(file,data):
    f = open(file, "w")
    for i in data:
        f.write(i+"\n")
    f.close()

try:
    f = open(notebook,"r")
    notes = f.readlines()
    f.close()
except IOError:
    f = open(notebook,"w+")
    f.close()
    print("No default notebook was found, created one.")

    

while True:
    print("Now using file "+str(notebook))
    print("(1) Read the notebook")
    print("(2) Add note")
    print("(3) Empty the notebook")
    print("(4) Change the notebook")
    print("(5) Quit\n")

    select = input("Please select one: ")
    select = int(select)
    save(notebook, notes)

    if select == 1:
        temp = ""
        for i in notes:
            temp += i
        print(temp)

    elif select == 2:
        note = input("Write a new note: ")
        notes.append(note+":::"+time.strftime("%X %x"))

    elif select == 3:
        notes = []
        print("Notes deleted.")

    elif select == 4:
        notebook = input("Give the name of the new file: ")
        print("notebook: "+notebook)
        
        try:
            f = open(notebook,"r")
            notes = f.readlines()
            f.close()

        except IOError:
            f = open(notebook,"w+")
            f.close()
            print("No notebook with that name detected, created one.")

    elif select == 5:
        save(notebook, notes)
        print("Notebook shutting down, thank you.")
        break

    

items = ["keksi","leipä","meetvursti","kana"]
items = []

while True:
    print("Would you like to \n(1)Add or\n(2)Remove items or\n(3)Quit?: ")
    select = int(input())

    if select == 1:
        item = input("What will be added?: ")
        items.append(item)

    elif select == 2:
        print("There are {x} items in the list.".format(x=len(items)))
        temp = int(input("Which item is deleted?: "))
        if temp < len(items) and temp >= 0:
            items.pop(temp)
        else:
            print("Incorrect selection.")

    elif select == 3:
        print("The following items remain in the list: ")
        for i in items:
            print(i)
        break
    else:
        print("Incorrect selection.")

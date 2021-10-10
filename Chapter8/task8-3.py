'''
The third exercise in the chapter continues with the calculator exercises done earlier. This time the idea is to finally take out the annoying problems with numbers, input validity and the stability problems caused by type conversion funvtion.


Make the following changes to the calculator: Every time the user gives numbers to the program, the system asks for the numbers with the prompt "Give a number: " and continues until a valid number is given. If the number is not correct, the system gives an error message "This input is invalid.". If the calculator works correctly, it prints out the following:



##########################	
>>> 
Calculator
Give a number: hah, NEVER
This input is invalid.
Give a number: What?
This input is invalid.
Give a number: 100
Give a number: Just kidding
This input is invalid.
Give a number: 50
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 100 50
Please select something (1-6): 2
The result is: 50
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 100 50
Please select something (1-6): 8
Thank you!
>>> 
###################################

The easiest way of implementing this feature is probably to define a separate function to call when asking numbers. In this function, an iteration keeps asking a number as long as the user decides to joke around. If the input is valid, iteration terminates with break and the function returns an acceptable value.


Example output:
#######################
Calculator
Give a number: 10
Give a number: test
This input is invalid.
Give a number: 2
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 10 2
Please select something (1-6): 5
The result is: -0.9589242746631385
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 10 2
Please select something (1-6): 6
The result is: 0.28366218546322625
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 10 2
Please select something (1-6): 8
Thank you!
#######################

'''

import math

selectGood = True #Jos väärä inputti niin piilotetaan joitain asioita tulostuksesta.
print("Calculator")

while True:
    num1 = input("Give a number: ")
    if num1.isnumeric():
        num1 = int(num1)
        break;
    else:
        print("This input is invalid.")

while True:
    num2 = input("Give a number: ")
    if num2.isnumeric():
        num2 = int(num2)
        break;
    else:
        print("This input is invalid.")

while True:


    
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7) Change numbers\n(8) Quit")
    print("Current numbers: "+str(num1)+" "+str(num2))
    select = int(input("Please select something (1-6): "))
    

    result = 0
    if select == 1:
        result = num1 + num2
        selectGood = True
    elif select == 2:
        result = num1 - num2
    elif select == 3:
        result = num1 * num2
    elif select == 4:
        result = num1 / num2
    elif select == 5:
        result = math.sin(num1/num2)
    elif select == 6:
        result = math.cos(num1/num2)

    elif select == 7:
       # print("Current numbers: "+str(num1)+" "+str(num2))
        #print("Change numbers")
        num1 = int(input("Give a number: "))
        num2 = int(input("Give a number: "))
        selectGood = False
        
    elif select == 8:
        print("Thank you!")
        break;
    else:
        print("Selection was not correct.")
        selectGood = False

    if selectGood == True:
        print("The result is: "+str(result))




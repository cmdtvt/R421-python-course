'''
The last exercise in this chapter continues with the exercise from the last chapter, the calculator. In this exercise, expand the existing code by implementing the following new features: (A) Calculator does not automatically quit when the result is given, allowing user to do new calculations. The user has to select "6" in the menu to exit the program. (B) The calculator shows the selected numbers in the main menu by printing "Current numbers:" and the user-given input. By selecting "5" in the calculator menu, the user can change the given numbers. When implemented correctly, the program prints out following:



############################
Calculator
Give the first number: 100
Give the second number: 25
(1) +
(2) -
(3) *
(4) /
(5) Change numbers
(6) Quit
Current numbers: 100 25
Please select something (1-6): 5
Give the first number: 10
Give the second number: 30

(1) +
(2) -
(3) *
(4) /
(5) Change numbers
(6) Quit
Current numbers: 10 30
Please select something (1-6): 1
The result is: 40

(1) +
(2) -
(3) *
(4) /
(5) Change numbers
(6) Quit
Current numbers: 10 30
Please select something (1-6): 6
Thank you!
>>> 
############################


Again, implement the program within one large while True-segment, which is terminated with break if the user selects the option "6".

############################
Example output:
Calculator
Give the first number: 50
Give the second number: 5
(1) +
(2) -
(3) *
(4) /
(5)Change numbers
(6)Quit
Current numbers: 50 5
Please select something (1-6): 1
The result is: 55
(1) +
(2) -
(3) *
(4) /
(5)Change numbers
(6)Quit
Current numbers: 50 5
Please select something (1-6): 2
The result is: 45
(1) +
(2) -
(3) *
(4) /
(5)Change numbers
(6)Quit
Current numbers: 50 5
Please select something (1-6): 4
The result is: 10.0
(1) +
(2) -
(3) *
(4) /
(5)Change numbers
(6)Quit
Current numbers: 50 5
Please select something (1-6): 6
Thank you!
############################

'''

selectGood = True
while True:
    print("Calculator")

    if selectGood == True:
        num1 = int(input("Give the first number: "))
        num2 = int(input("Give the second number: "))

    selectGood = True
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5) Change numbers\n(6) Quit")
    select = int(input("Please select something (1-6): "))

    result = 0
    if select == 1:
        result = num1 + num2
    elif select == 2:
        result = num1 - num2
    elif select == 3:
        result = num1 * num2
    elif select == 4:
        result = num1 / num2
    elif select == 5:
        print("Change numbers")
        num1 = int(input("Give the first number: "))
        num2 = int(input("Give the second number: "))
        selectGood = False
        
    elif select == 6:
        break;
    else:
        print("Selection was not correct.")
        selectGood = False

    if selectGood == True:
        print("The result is: "+str(result))




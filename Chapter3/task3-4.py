'''
In the fourth exercise the idea is to define an if-structure which decides the action based on several inputs. The program asks for two numbers. If both of the numbers are even, the program prints "Both numbers are even." If only one of the numbers is even, the program prints "One of the numbers is even.". Finally, if neither of the numbers is even, the program prints "Both numbers are odd". When correct, the program works as following:


###########
Give a number: 10
Give another number: 11
One of the numbers is even.
###########

or alternatively

###########
Give a number: 12
Give another number: 20
Both numbers are even.
###########

or alternatively

###########
Give a number: 15
Give another number: 21
Both numbers are odd.

Example output:
Give a number: 7
Give another number: 9
Both numbers are odd.
###########
'''


num = int(input("Give a number: "))
num2 =  int(input("Give another number: "))


if (num %2 == 0 and num2 %2 == 0):
    print("Both numbers are even.")
elif (num %2 != 0 and num2 %2 != 0):
    print("Both numbers are odd.")
elif num %2 == 0 or num2 %2 == 0:
    print("One of the numbers is even.")


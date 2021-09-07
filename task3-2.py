'''
The second exercise takes another step towards more realistic programming structures. In this exercise the idea is to create an if-structure, which has another if-structure inside it. Basically the idea is to implement the following structure:

#########################
if [selection]:
	[code]
	
	if [selection]:
		[code]
	else:
		[code}
else:
	[code]
#########################

The idea is to create a program which asks for a user name and password. If the given name is wrong, the program prints "The given name is wrong". If the name is acceptable, the program asks for the password. If the password is correct, the system prints "Both inputs are correct!", otherwise "The password is incorrect.". The correct inputs should be "John" and the password "ABC123". Overall, the program should print the following:


#########################
Give name: Peter
The given name is wrong.
#########################

or alternatively

#########################
Give name: John
Give password: Monkeys?
The password is incorrect.
#########################

or alternatively

#########################
Give name: John
Give password: ABC123
Both inputs are correct!
#########################

'''



resp = ""
if input("Give name: ") == "John":
    if input("Give password: ") == "ABC123":
        resp = "Both inputs are correct!"
    else:
        resp = "The password is incorrect."
else:
    resp = "The given name is wrong."


print(resp)
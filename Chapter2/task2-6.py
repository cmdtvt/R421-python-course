'''
The last exercise in this chapter focuses on string slices. Define a variable and assign it a string "desserts" as a value. Then create three new variables, and assign them values by slicing the A) first 4 characters B) the last 4 characters and C) the entire string backwards as given values. Then make the program print the answers in the following way:

########
The first 4 characters were: dess
The last 4 characters were: erts
The string backwards was: stressed
########

'''



var = "desserts"

a = var[0:4]
b = var[-4:]
c = var[::-1]

print("The first 4 characters were: "+a)
print("The last 4 characters were: "+b)
print("The string backwards was: "+c)
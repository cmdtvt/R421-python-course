'''
In this exercise the aim is to try out different datatypes. Start by defining two variables, and assign the first variable the float value 10.6411. The second variable gets a string "Stringline!" as a value.
'''

var1 = 10.6411
var2 = "Stringline!"

var1 = int(var1)
var2 = var2*2

print("Integer conversion cannot do roundings: "+str(var1))
print("Multiplying strings also causes trouble: "+str(var2))
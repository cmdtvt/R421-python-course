'''
Unsurprisingly, the second exercise in this chapter discusses the task of writing to a file. Create a program which prompts the user for a file name "Give a file name: " and then for an input "Write something: ". After this, the program writes the string given by the user to the file and reports "Wrote [input] to the file [name].". When working correctly, the program prints something like this:

 


####################
>>> 
Give a file name: log.txt
Write something: Attencion, attencion. 10, 10, 22, 33, Adios.
Wrote Attencion, attencion. 10, 10, 22, 33, Adios. to the file log.txt.
>>>  
####################


Example output:
####################
Give a file name: test.txt
Write something: This is test.
Wrote This is test.  to the file test.txt
####################
'''

fn = input("Give a file name: ")
wr = input("Write something: ")

f = open(fn, "a")
f.write(wr)
f.close()

print("Wrote "+wr+" to the file"+fn)



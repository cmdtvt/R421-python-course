



file = "words.txt"
data = []
try:
    f = open(file,"r")
    for i in f.readlines():
        data.append(i.strip())
    f.close()
except IOError:
    print("Error")


data = sorted(data)
print("Words in an alphabetical order:")
for i in data:
    print(i)
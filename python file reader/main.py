
myList = []
myFile = open('text.txt', 'r')

myList = myFile.read().splitlines()

print(myList)
def printAbove(intArray, number):
    countAbove=0 
    countBelow=0
    for integer in intArray:
        if integer > number:
            countAbove = countAbove + 1
        elif integer < number:
            countBelow = countBelow + 1
    print("Above:",countAbove,", Below:",countBelow)
        
#You didn't say what to do with numbers that are equal to given so they are ignored

def rotateStr(intStr, rotateBy):
    newStr = ""
    for iterator in range(0,len(intStr)):
        index = len(intStr)-rotateBy+iterator
        if index > len(intStr)-1:
            index = index - len(intStr) 
        newStr = newStr + (intStr[index])
    print(newStr)


printAbove( [1, 5, 2, 1, 10],6)
rotateStr("MyString", 2)

# I'm not sure what I would change about Java, but something I like about Python
# is how it's built off of indenting, so that sort of forces you to make it 
# more readable. In Java you can have a one line if statement without {}, but
# I put them there anyway to be sure.


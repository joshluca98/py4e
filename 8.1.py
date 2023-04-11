def chop(myList):
    # remove first and last elements of list
    del myList[0]
    del myList[len(myList) - 1]
    print(myList)
    # return None
    return None

def middle(myList):
    # copy list into new list
    newList = myList[:]
    # return new list with first and last element removed
    del newList[0]
    del newList[len(newList) - 1]
    print(newList)
    return newList

myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(myList)
chop(myList)
middle(myList)
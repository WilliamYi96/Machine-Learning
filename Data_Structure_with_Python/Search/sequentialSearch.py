def sequentialSearch(aList, item):
    pos = 0
    found = False

    while pos < len(aList) and not found:
        if aList[pos] == item:
            found = True
        else:
            pos += 1
    
    return found

testList = [1,2,3,4,5,6]
print(sequentialSearch(testList, 3))
print(sequentialSearch(testList, 7))
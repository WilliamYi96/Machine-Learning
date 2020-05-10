def orderedSequentialSearch(aList, item):
    pos = 0
    found = False
    stop = False
    while pos < len(aList) and not found and not stop:
        if aList[pos] == item:
            found = True
        else:
            if aList[pos] > item:
                stop = True
            else:
                pos = pos + 1
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(orderedSequentialSearch(testlist, 3))
print(orderedSequentialSearch(testlist, 13))
def binarySearch(aList, item):
    left = 0
    right = len(aList) - 1
    found = False

    while left <= right and not found:
        mid = (left + right) / 2
        if aList[mid] == item:
            found = True
        elif aList[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    
    return found

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
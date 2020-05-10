# Sequential Search: Time O(n), Space O(1)
def sequentialSearch(aList, target):
    for i in range(len(aList)):
        if aList[i] == target:
            return i
    return False

# early break sequential search: Time O(n), Space O(1)
def earlyBreakSequentialSearch(aList, target):
    for i in range(len(aList)):
        if aList[i] == target:
            return i
        elif aList[i] > target:
            return False
    return False

# binary search: Time O(logn), Space O(1)
def binarySearch(aList, target):
    left = 0
    right = len(aList) - 1
    while left <= right:
        mid = (left + right) >> 1
        if aList[mid] == target:
            return mid
        elif aList[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

testList = [1,2,3,4,5,6]
print(sequentialSearch(testList, 3))
print(sequentialSearch(testList, 7))
print(earlyBreakSequentialSearch(testList, 3))
print(earlyBreakSequentialSearch(testList, 7))
print(binarySearch(testList, 3))
print(binarySearch(testList, 7))
# For recursion, the most import part is to find recursive equation

# Three laws of recursion
# A recursive algorithm must have a base case.
# A recursive algorithm must change its state and move toward the base case.
# A recursive algorithm must call itself, recursively.

def listSum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listSum(numList[1:])

print(listSum([1,2,3,4,5,6]))
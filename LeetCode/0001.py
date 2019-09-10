# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Solved on 09/10/2019 by William

def twoSum(aList, target):
    values = {}
    for i in range(len(aList)):
        needed_value = target - aList[i]
        if needed_value in values:
            return [values[needed_value], i]
        values[aList[i]] = i
        print(values)
    raise Exception('Not Found!')

aList = [2,7,11,15]
target = 9
print(twoSum(aList, target))


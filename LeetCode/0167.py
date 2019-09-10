"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

# Solved on 09/10/2019 by William"""

def twoSum(numbers, target):
    values = {}
    for i in range(len(numbers)):
        needed_value = target - numbers[i]
        # print(needed_value, values)
        # if needed_value < 0:
        #     raise Exception("Match Not Found!")
        if needed_value in values:
            return [values[needed_value]+1, i+1]
        values[numbers[i]] = i 
    raise Exception("Match Not Found!")

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers, target))
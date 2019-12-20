# Greedy algorithm

class Solution:
    def intToRoman(self, num):
        nums    = [1000,900, 500,400, 100, 90, 50,  40, 10,  9,   5,  4,   1 ]
        symbols = ['M', 'CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        mstr = ''
        for i in range(len(nums)):
            while num >= nums[i]:
                mstr += symbols[i]
                num -= nums[i]
        return mstr

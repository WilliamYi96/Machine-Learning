class Solution:
    def romanToInt(self, s):
        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M' ]
        values  = [ 1 ,  5 ,  10,  50, 100, 500, 1000]
        sum = 0

        i = 0
        while i < len(s):
            curValue = values[symbols.index(s[i])]
            if i == len(s)-1:
                sum += curValue      
                return sum
            nextValue = values[symbols.index(s[i+1])]
            if curValue < nextValue:
                i += 1
                sum += (nextValue - curValue)
                if i == len(s) - 1:
                    return sum
            else:
                sum += curValue
            i += 1
        return sum
        

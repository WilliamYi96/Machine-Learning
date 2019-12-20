class Solution:
    def distributeCandies(self, candies, num_people):
        disList = [0] * num_people
        i = 0
        res = candies

        while True:
            i += 1
            if res > i:
                mindex = int((i-1)%num_people)
                num_people[mindex] += i
                res = res - i
            else:
                mindex = int(i%num_people)
                num_people[mindex] += res
                return disList

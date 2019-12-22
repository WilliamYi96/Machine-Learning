class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mlength = len(intervals)
        i = j = 0
        Shuffle = False
        while i< mlength:
            while j < mlength:
                if j==i:
                    continue
                a1, b1 = intervals[i][0], intervals[j][0]
                a2, b2 = intervals[i][1], intervals[j][1]   
                print(a1, b1, a2, b2)
                if b1<a1 and a1<b2:
                    intervals.remove([a1, a2], [b1, b2])
                    intervals.append([b1, a2])
                    Shuffle = True
                elif a1<b1 and b1<a1:
                    intervals.remove([a1, a2], [b1, b2])
                    intervals.append([a1, b2])
                    Shuffle = True
                if Shuffle:
                    mlength = len(intervals)
                    i = j = 0
                    Shuffle = False
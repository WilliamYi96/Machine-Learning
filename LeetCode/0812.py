class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxArea = 0
        for i in range(len(points)):
            for j in range(i, len(points)):
                for k in range(j, len(points)):
                    curArea = self.Shoelace(points, i, j, k)
                    if curArea > maxArea:
                        maxArea = curArea
        return maxArea
    
    def Shoelace(self, points, i, j, k):
        curArea = 0.5* abs((points[i][0]*points[j][1]
                            +points[j][0]*points[k][1]
                            +points[k][0]*points[i][1]) -
                            (points[i][1]*points[j][0]
                            +points[j][1]*points[k][0]
                            +points[k][1]*points[i][0]))
        print(curArea)
        return curArea
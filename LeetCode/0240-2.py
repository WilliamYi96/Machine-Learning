class Solution:
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        left, top = 0, 0
        right, down = len(matrix[0])-1, len(matrix)-1

        if target < matrix[top][left] or target > matrix[down][right]:
            return False

        while left<=len(matrix[0])-1 and down>=0:
            # print(down, left)
            curPoint = matrix[down][left]
            if curPoint == target:
                return True
            elif curPoint > target:
                down -= 1
            elif curPoint < target:
                left += 1
        return False

# [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
# 20
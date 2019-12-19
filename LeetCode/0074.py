# class Solution:
#     def searchMatrix(self, matrix, target):
#         top = 0
#         bottom = len(matrix) - 1
#         if bottom < 0:
#             return False
#         while top <= bottom:
#             mid = top + ((bottom - top) >> 1)
#             left = 0
#             right = len(matrix[0]) - 1
#             if right < 0:
#                 return False
#             if matrix[mid][0] == target:
#                 return True
#             elif matrix[mid][0] > target:
#                 bottom = mid - 1
#             elif matrix[mid][0] < target:
#                 while left <= right:
#                     rowMid = left + ((right - left) >> 1)
#                     if matrix[mid][rowMid] == target:
#                         return True
#                     elif matrix[mid][rowMid] > target:
#                         right = rowMid - 1
#                     elif matrix[mid][rowMid] < target:
#                         left = rowMid + 1
#                 top = mid + 1
#         return False       

class Solution:
    def searchMatrix(self, matrix, target):
        left = 0
        row = len(matrix)
        if row == 0:
            return False
        col = len(matrix[0])
        right = row * col - 1
        while left <= right:
            mid = (left + right) >> 1
            nrow = mid / col       
            ncol = mid % col
            if matrix[nrow][ncol] == target:
                return True
            elif matrix[nrow][ncol] > target:
                right = mid - 1
            elif matrix[nrow][ncol] < target:
                left = mid + 1
        return False    

matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 9

sol = Solution()
print(sol.searchMatrix(matrix, target))
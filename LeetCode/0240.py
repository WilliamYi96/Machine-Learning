class Solution:
    def binary_search(self, matrix, vertical, i, target):
        lo = 0
        hi = len(matrix[0])-1 if vertical else len(matrix)-1

        if vertical:
            while lo <= hi:
                mid = (lo + hi) >> 1
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return False
        else:
            while lo <= hi:
                mid = (lo + hi) >> 1
                if matrix[mid][i] == target:
                    return True
                elif matrix[mid][i] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return False
                    

    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        # print('Checkpoint One Pass') # Pass

        for i in range(min(len(matrix), len(matrix[0]))):
            # print('i = {}'.format(i))
            vertical_found = self.binary_search(matrix, True, i, target)
            horizontal_found = self.binary_search(matrix, False, i, target)
            # print('Checkpoint Two:')
            # print(vertical_found, horizontal_found)

            if vertical_found or horizontal_found:
                return True
        return False
                
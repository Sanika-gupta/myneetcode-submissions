class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
         # rows
        top = 0
        btm = ROWS - 1
        while top <= btm:
            # want the middle row 
            row = (top+btm) // 2
           # If target is greater than the last element of the row, go down
            if target > matrix[row][-1]:
                top = row + 1
            # If target is smaller than the first element of the row, go up
            # CHANGE: Use < instead of <=. If target == matrix[row][0], we break and search this row.
            elif target < matrix[row][0]:
                btm = row - 1
            else:
                # The target must be in this row
                break
        if not(top<= btm):
            return False
        # 2nd binary search portion, run BINARY SEARCH ON THE ROW 
        row = (top+btm) // 2
        l = 0
        r = COLS - 1 # rightmost value in row
        while (l<=r):
            # middle point 
            mid = (l + r )//2
            if target>matrix[row][mid]:
                # move rightards
                l = mid +1
            elif target<matrix[row][mid]:
                # move rightards
                r = mid - 1
            else:
                return True
        return False





        
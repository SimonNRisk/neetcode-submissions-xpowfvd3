class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        2d matrix
        target int
        each row is in non-decreasing (increasing or constant) order
        first int of row 2 is greater than last int of row 1

        1st determine row
        2nd determine col


        1) determine row:
        top, bot = 0, len(matrix)-1

        while top < bot:
            mid = (top+bot)/ 2
            mid_el = matrix[mid][0]

            # if greater, could be in this row or lower
            # if less, must be in lower row
            if mid_el > target:
                bot = top-1
            elif mid_el < target:
                top = bot
            else:
                return True
            
            2) just do binary search on matrix[top]
        '''
        if not matrix:
            return False
        # determine row
        top, bot = 0, len(matrix)-1
        while top <= bot:
            mid = (top+bot)//2
            mid_el = matrix[mid][0]

            if mid_el > target:
                bot = mid -1
            elif mid_el < target:
                top = mid +1
            else:
                return True
        
        if bot < 0:
            return False
        
        # bot now has the row
        
        # determine col
        row = matrix[bot]
        left, right = 0, len(row)-1
        while left <= right:
            mid = (left+right)//2
            if row[mid] == target:
                return True
            elif  row[mid] < target:
                left = mid +1
            else:
                right = mid-1

        return False
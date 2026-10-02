class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Given nums
        # non-decreasing order (increasing or same)
        # Return array of squares of each, sorted
        # Need to consider negatives
        '''
        I wonder if we do a two pointer thing?
        We know that the left most and right most 

        Obvious solution:
        put all squares in a list: O(n)
        sort the list: O(nlogn)
        '''
        # Or just do the max way, then reverse
        left = 0
        right = len(nums)-1

        result = []

        while left <= right:
            left_val = abs(nums[left])
            right_val = abs(nums[right])
            print(f"left:{left_val}, right:{right_val}")
            if right_val > left_val:
                result.append((right_val**2))
                right -=1
            else:
                result.append((left_val**2))
                left +=1
        return result[::-1]

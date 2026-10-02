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
        result = []
        for num in nums:
            result.append((num*num))
        return sorted(result)
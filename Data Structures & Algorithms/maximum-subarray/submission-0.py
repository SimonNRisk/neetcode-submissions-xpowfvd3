class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        nums = [int]
        contiguous subarray with largest sum
        return sum

        my thinking here is that if the next number
        is > 0, include it, else restart


        greedy question:
        at each number, we can:
            A) start a fresh running sum with this num
            B) add this num to our running sum
        
        choose whichever is better (greedy)
        '''
        run_sum = 0
        max_sum = float('-inf')
        for num in nums:
            if run_sum + num > num:
                run_sum += num
            else:
                run_sum = num
            max_sum = max(run_sum, max_sum)
        return max_sum
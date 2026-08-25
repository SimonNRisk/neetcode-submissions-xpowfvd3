class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        running_sum = 0
        for num in nums:
            if num == 1:
                running_sum +=1
                max_length = max(running_sum, max_length)
            # Assuming only get 1s and 0s
            else:
                running_sum = 0
        return max_length
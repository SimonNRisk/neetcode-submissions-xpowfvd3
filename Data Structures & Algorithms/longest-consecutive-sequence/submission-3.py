class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for num in nums_set:
            # first check if start
            if (num-1 in nums_set):
                continue
            # Now we are at start
            length = 0
            while (num+length) in nums_set:
                length+=1
            longest = max(longest, length)
        return longest
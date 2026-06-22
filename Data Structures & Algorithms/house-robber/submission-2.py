class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        cache = {}

        def recurse(idx):
            if idx >= n:
                return 0
            
            if idx in cache:
                return cache[idx]

            max_2 = recurse(idx+2)
            max_3 = recurse(idx+3)
            
            total = max(max_2, max_3)
            cache[idx] = total + nums[idx]
            return cache[idx]
        
        return max(recurse(0), recurse(1))
        
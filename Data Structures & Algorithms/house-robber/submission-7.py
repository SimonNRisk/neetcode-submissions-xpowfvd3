class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        prev = nums[0]
        curr = max(nums[0], nums[1])

        for i in range(2, n):
            prev, curr = curr, max(prev+nums[i], curr)
        return curr


        '''
        n = len(nums)
        cache = {}

        def recurse(idx):
            if idx == 0:
                return nums[0]
            if idx == 1:
                return max(nums[0], nums[1])
            
            if idx in cache:
                return cache[idx]
            
            total = max(recurse(idx-1), recurse(idx-2) + nums[idx])
            cache[idx] = total
            return cache[idx]
        
        return recurse(n-1)
        '''
        
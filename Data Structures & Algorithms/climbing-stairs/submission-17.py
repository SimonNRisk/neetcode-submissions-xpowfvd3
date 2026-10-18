class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Top down:
        have a fn that takes num, returns cache[num]

        '''
        '''
        Bottom up:
        cache = {1: 1, 2:2}
        if n in cache:
            return cache[n]
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]
        '''
        cache = {1: 1, 2:2}
        def dp(num):
            if num in cache:
                return cache[num]
            result = dp(num-1) + dp(num-2)
            cache[num] = result
            return result
        return dp(n)






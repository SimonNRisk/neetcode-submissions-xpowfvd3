class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 
        # we only care about the last 2 numbers
        prev = 1
        cur = 2
        for _ in range(2, n+1):
            prev, cur = cur, cur+prev

        return prev



        
        
        '''
        cache = {1:1, 2:2}
        def f(x):
            if x in cache:
                return cache[x]
            cache[x] = f(x-1) + f(x-2)
            return cache[x]
        return f(n)
        '''
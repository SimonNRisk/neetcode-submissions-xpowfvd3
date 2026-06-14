class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        print(dp)
        return dp[n-1]



        
        
        '''
        cache = {1:1, 2:2}
        def f(x):
            if x in cache:
                return cache[x]
            cache[x] = f(x-1) + f(x-2)
            return cache[x]
        return f(n)
        '''
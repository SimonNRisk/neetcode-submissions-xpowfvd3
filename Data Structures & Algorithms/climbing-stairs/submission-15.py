class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        n steps to reach top
        can take either 1 or 2
        # of distinct ways?
        n = 3
        can do:
        1, 1, 1
        2, 1
        1, 2

        n = 2:
        2
        1, 1
        
        n = 1
        1

        n =3 is n= 2 + n=1
        '''
        cache = {1: 1, 2:2}
        if n in cache:
            return cache[n]
        for i in range(3, n+1):
            cache[i] = cache[i-1] + cache[i-2]
        return cache[n]






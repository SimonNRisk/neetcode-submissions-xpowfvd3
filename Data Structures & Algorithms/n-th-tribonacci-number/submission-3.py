class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        last, prev, cur = 0, 1, 1

        for _ in range(3, n+1):
            last, prev, cur = prev, cur, last+prev+cur
        
        return cur







        '''
        cache = {0:0, 1:1, 2:1}

        def recurse(num):
            if num in cache:
                return cache[num]
            else:
                value = recurse(num-3) + recurse(num-2) + recurse(num-1)
                cache[num] = value
                return cache[num]
            return value
        
        return recurse(n)
        '''
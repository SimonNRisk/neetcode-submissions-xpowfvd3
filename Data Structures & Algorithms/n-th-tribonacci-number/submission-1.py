class Solution:
    def tribonacci(self, n: int) -> int:
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
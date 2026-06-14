class Solution:
    def climbStairs(self, n: int) -> int:
        # first solve recursively
        # top down (memoize)
        # bottom up (tabular) - typically preferred
        # what are the bases cases?
        cache = {1:1, 2:2}
        def f(x):
            if x in cache:
                return cache[x]
            cache[x] = f(x-1) + f(x-2)
            return cache[x]
        return f(n)
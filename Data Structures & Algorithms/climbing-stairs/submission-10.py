class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {1:1, 2:2}
        def recurse(level):
            if level in cache:
                return cache[level]
            cache[level] = recurse(level-1) + recurse(level-2)
            return cache[level]
        return recurse(n)
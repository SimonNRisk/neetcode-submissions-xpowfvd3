class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        prev, cur = 1, 2
        for i in range(3, n+1):
            prev, cur = cur, prev+cur
        return cur
        # note - this only depends on the prev 2 things

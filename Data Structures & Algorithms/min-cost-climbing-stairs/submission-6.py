class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # top down
        n = len(cost)
        memo = {0: 0, 1: 0}
        def recurse_cost(idx):
            if idx in memo:
                return memo[idx]
                # it is free to get to either idx 0 or 1
            memo[idx] = min(
                (recurse_cost(idx-1) + cost[idx-1]),
                (recurse_cost(idx-2)+cost[idx-2])
                )
            return memo[idx]
        return recurse_cost(n)



        # recursive brute force

        '''
        At 3 (index 2), the min cost to get there is the min cost
        to get to index 1 + value @ 1 or the min cost to get to index 0 + value @ 0
        '''
        # This works! but too slow
        '''
        n = len(cost)
        def recurse_cost(idx):
            if idx < 2:
                return 0
                # it is free to get to either idx 0 or 1
            return min(
                (recurse_cost(idx-1) + cost[idx-1]),
                (recurse_cost(idx-2)+cost[idx-2])
                )
        return recurse_cost(n)
        '''




        '''
        # I know wonder if, because we are only looking at i-1 and i-2, if we can do it in constant time
        n = len(cost)
        prev, cur = 0, 0
        for i in range(2, n+1):
            prev, cur = cur, min((prev+cost[i-2], cur+cost[i-1]))
        return cur
        '''
        # this is optimal - O(n) time and o(1) space, but let's go
        # for the recursive and topdown ones as well







        '''
        n = len(cost)
        dp = [0] * (n+1)
        # each dp entry is the min cost to get there
        # want the min cost to get to n-index (one out)
        for i in range(2, n+1):
            dp[i] = min((dp[i-1] + cost[i-1]), dp[i-2]+ cost[i-2])
        return dp[n]
        '''

        
        
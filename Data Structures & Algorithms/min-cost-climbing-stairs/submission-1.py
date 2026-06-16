class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # I know wonder if, because we are only looking at i-1 and i-2, if we can do it in constant time
        n = len(cost)
        prev, cur = 0, 0
        for i in range(2, n+1):
            prev, cur = cur, min((prev+cost[i-2], cur+cost[i-1]))
        return cur

        # imagine for 1, 2, 3
        # prev, cur =0, 1
        # prev, cur = 1, min(2, 1+3)
        # prev, cur = 1, 2





        '''
        n = len(cost)
        dp = [0] * (n+1)
        # each dp entry is the min cost to get there
        # want the min cost to get to n-index (one out)
        for i in range(2, n+1):
            dp[i] = min((dp[i-1] + cost[i-1]), dp[i-2]+ cost[i-2])
        return dp[n]
        '''

        
        
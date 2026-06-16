class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n+1)
        # each dp entry is the min cost to get there
        # want the min cost to get to n-index (one out)
        for i in range(2, n+1):
            dp[i] = min((dp[i-1] + cost[i-1]), dp[i-2]+ cost[i-2])
        return dp[n]

        
        
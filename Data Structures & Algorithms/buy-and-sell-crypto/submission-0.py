class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #highest day in future, keep track of min thus far
        min_buy = float('inf')
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price - min_buy)
            min_buy = min(min_buy, price)
        return max_profit
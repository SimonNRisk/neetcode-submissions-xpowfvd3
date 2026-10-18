class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        int array coins (unlimited number of each)
        int amount

        return fewest coins to make up exact target amount

        add to itself or move to next

        if we have sorted coins, we can eitehr get change from using prev result, or for using that coin


        can have map of ways to get each denomination, up to amount
        [0...amount]

        fewest coins to get amount:
            for each coin:
                the coin itself
                OR
                the coin + the min way to get the difference
                OR 
                cant
        '''

        '''
        bottom up?
        make cache from 0 to the amount
        ways to make n are:
            loop over coins
            if coin == it, set cache[n] = 1
            else:
                it will be in cache in nonnegatie so get from there
            after looping over each coin, set to minn
        '''
        cache = {0:0}
        coins.sort()
        for i in range(1, amount+1):
            minn = float("inf")
            for coin in coins:
                diff = i - coin
                if diff < 0:
                    cache[i] = minn
                    break
                minn=min(minn,1 + cache[diff])
            cache[i] = minn
        result = cache[amount]
        if result < float("inf"):
            return cache[amount]
        return -1





        '''
        coins.sort()
        memo = {0:0}
        def dfs(amt):
            minn = float("inf")
            if amt in memo:
                return memo[amt]

            for coin in coins:
                diff = amt - coin
                if diff < 0:
                    break # minn would be inf, meaning we cant make it
                # can make it
                minn = min(minn, 1 + dfs(diff))
            memo[amt] = minn
            return minn
        result = dfs(amount)
        if result < float("inf"):
            return result
        else:
            return -1
            '''








                
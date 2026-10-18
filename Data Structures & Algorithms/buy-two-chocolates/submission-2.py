class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        '''
        given int prices (price of diff chocolates in store)
        given int money (initial amount of money)
        want to buy 2 chocolates such that have non-negative leftover money
        minimize the sum of the prices
        return left over money
        if no option, return
        '''
        cheapest = float("inf")
        second_cheapest = float("inf")
        for price in prices:
            if price < cheapest:
                second_cheapest = cheapest
                cheapest = price
            elif price < second_cheapest:
                second_cheapest = price
        total = cheapest+second_cheapest
        if total > money:
            return money
        return money - total

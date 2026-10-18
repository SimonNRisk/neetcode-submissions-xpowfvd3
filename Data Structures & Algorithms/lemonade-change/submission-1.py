from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        '''
        each lemondae is $5
        customers stand in queue to buy from you
        order one at a time (bill)
        must provide correct change so net transaction is $5
        have originally no change in hand
        true if can, false if cant


        ONLY 5 10 20

        if its 5, done
        if it's 10, we MUST have a 5
        if it's 20, we MUST have either:
            10 and 5
            three 5s

        can_pay = True

        Plan:
        loop through bills
            if bill == 5:
                continue
            add bill we receive to a freq map
            if bill == 10:
                num_fives = freq_map.get(5, 0)
                if num_fives <= 0:
                    can_pay = false
                    break
                else:
                    freq_map[5] -=1
            if bill -==
            
                    
        '''
        can_pay = True
        freq_map = defaultdict(int)
        for bill in bills:
            freq_map[bill] +=1
            if bill == 10:
                num_fives = freq_map[5]
                if num_fives <= 0:
                    can_pay = False
                    break
                else:
                    freq_map[5] -=1
            if bill == 20:
                num_tens = freq_map[10]
                num_fives = freq_map[5]
                if num_tens > 0 and num_fives > 0:
                    freq_map[10] -=1
                    freq_map[5] -=1
                elif num_fives >= 3:
                    freq_map[5] -=3
                else:
                    can_pay = False
                    break
        return can_pay


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_min = 1
        cur_max = 1
        res = nums[0]
        for num in nums:
            if num == 0:
                res = max(res, num)
                cur_min = 1
                cur_max = 1
            else:
                temp = cur_max
                cur_max = max(num, cur_max*num, cur_min*num)
                cur_min = min(num, temp*num, cur_min*num)
                res = max(cur_max, cur_min, res)
                '''
            print(f"max: {cur_max}")
            print(f"min: {cur_min}")
            print(f"res: {res}")
            '''
        return res

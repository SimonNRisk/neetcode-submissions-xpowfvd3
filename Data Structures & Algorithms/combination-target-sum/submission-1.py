class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        def backtrack(idx, cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return
            if cur_sum > target or idx == n:
                return

            backtrack(idx+1, cur_sum)

            sol.append(nums[idx])
            backtrack(idx, cur_sum + nums[idx])
            sol.pop()
            
        backtrack(0, 0)
        return res
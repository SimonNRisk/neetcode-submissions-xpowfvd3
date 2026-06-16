class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)

        def backtrack(idx, cur_sum):
            if idx >= n:
                return
            if cur_sum > target:
                return
            if cur_sum == target:
                res.append(sol[:])
                return
            
            # two choices
            # 1) do nothing and move on
            backtrack(idx+1, cur_sum)

            # 2) take it and stay
            sol.append(nums[idx])
            cur_sum += nums[idx]
            backtrack(idx, cur_sum)
            cur_sum -= nums[idx]
            sol.pop()
            return
        
        backtrack(0, 0)
        return res
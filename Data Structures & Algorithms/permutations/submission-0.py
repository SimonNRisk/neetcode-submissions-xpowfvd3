class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol  = [], []
        n = len(nums)
        def backtrack(idx):
            if len(sol) == n:
                res.append(sol[:])
                return

            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack(idx+1)
                    sol.pop()
            
            return

        backtrack(0)
        return res
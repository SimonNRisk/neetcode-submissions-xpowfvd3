class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        
        def backtrack(idx):
            # basecase
            if idx == len(nums):
                res.append(sol[:])
                return
            
            backtrack(idx+1)

            sol.append(nums[idx])
            backtrack(idx+1)
            sol.pop()
            return
            

        backtrack(0)
        return res
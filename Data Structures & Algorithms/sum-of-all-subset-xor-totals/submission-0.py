class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        sol = []

        def backtrack(idx):
            nonlocal res
            if idx == len(nums):
                total = 0
                for val in sol:
                    total ^= val
                res += total
                return 
            
            # 2 decisions
            # stay empty
            backtrack(idx+1)
            
            # add whatever is at your index
            sol.append(nums[idx])
            backtrack(idx+1)
            sol.pop()
            return
        
        backtrack(0)
        return res
        



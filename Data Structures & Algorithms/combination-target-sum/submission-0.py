class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # options are take it or take the next
        res, sol = [], []
        # what is our base case?
        # we're tkaking either way, so base case is when sum of sol > target
        def backtrack(idx): #take an index to know what to take / what is next
            total = 0
            for val in sol:
                total += val
            if total == target:
                res.append(sol[:])
                return
            if total > target: #base case
                return
            if idx >= len(nums):
                return


            backtrack(idx+1)
            
            # two cases
            # take it
            sol.append(nums[idx])
            backtrack(idx)
            sol.pop()
            # take the next
            
        backtrack(0)
        return res
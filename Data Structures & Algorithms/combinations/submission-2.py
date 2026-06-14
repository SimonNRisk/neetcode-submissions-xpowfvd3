class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(idx):
            if len(sol) == k:
                res.append(sol[:])
                return
            
            if idx + len(sol) > k:
                backtrack(idx-1)

            sol.append(idx)
            backtrack(idx-1)
            sol.pop()
            return
        
        backtrack(n)
        return res
            


        
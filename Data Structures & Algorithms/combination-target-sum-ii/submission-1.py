class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res, sol = [], []

        def backtrack(idx, cur_sum):
            # base cases
            if cur_sum == target:
                res.append(sol[:])
                return
            if cur_sum > target or idx >= n:
                return
            # two pathes
            # if take, then move on
            # if skip, then skip all and move on
            sol.append(candidates[idx])
            backtrack(idx+1, cur_sum + candidates[idx])
            sol.pop()

            next_idx = idx + 1
            while next_idx < n and candidates[next_idx] == candidates[idx]:
                next_idx += 1

            backtrack(next_idx, cur_sum)
        
        backtrack(0, 0)
        return res
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        num_rows = len(grid)
        num_cols = len(grid[0])
        def dfs(r, c):
            if (r, c) in seen:
                return 0
            seen.add((r, c))
            # Check bounds
            if r < 0 or r > num_rows-1 or c < 0 or c > num_cols-1:
                return 0
            if grid[r][c] == 0:
                return 0
            if grid[r][c] == 1:
                return 1 + dfs(r, c+1) + dfs(r, c-1) + dfs(r+1, c) + dfs(r-1, c)
            return 0
        max_area = 0
        for r in range(num_rows):
            for c in range(num_cols):
                value = dfs(r, c)
                max_area = max(max_area, value)
        return max_area


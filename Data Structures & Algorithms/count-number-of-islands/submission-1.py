class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        num_rows = len(grid)
        num_cols = len(grid[0])
        seen = set()
        def dfs(r, c):
            if grid[r][c] != '1':
                return 0
            if (r, c) in seen:
                return 0
            seen.add((r, c))
            # now go up down left right
            # Up
            if r > 0:
                dfs(r-1, c)
            # Down
            if r < num_rows -1:
                dfs(r+1, c)
            # Left
            if c > 0:
                dfs(r, c-1)
            # Right
            if c < num_cols-1:
                dfs(r, c+1)
            return 1

        result= 0

        for r in range(num_rows):
            for c in range(num_cols):
                result += dfs(r, c)
        return result

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        perimeter = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 0:
                    pass
                else:
                    # check left right up down
                    num_sides = 4
                    if c > 0 and grid[r][c-1] == 1:
                        num_sides -=1
                    if c < num_cols-1 and grid[r][c+1] == 1:
                        num_sides -=1
                    if r > 0 and grid[r-1][c] == 1:
                        num_sides -=1
                    if r < num_rows -1 and grid[r+1][c] ==1:
                        num_sides -=1
                    perimeter += num_sides
        return perimeter
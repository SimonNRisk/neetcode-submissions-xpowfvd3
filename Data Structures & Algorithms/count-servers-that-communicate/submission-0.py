class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        # Preprocess columns
        count_per_row = [0] * num_rows
        count_per_col = [0] * num_cols
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1:
                    count_per_row[r] +=1
        for c in range(num_cols):
            for r in range(num_rows):
                if grid[r][c] == 1:
                    count_per_col[c] +=1
        
        
        # Now that we have count per each
        # Iterate through again
        # Check both col and row
        # If > 0, increment
        print(count_per_row)
        print(count_per_col)
        num_communicates = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1 and (count_per_row[r] > 1 or count_per_col[c] > 1):
                    num_communicates += 1
        return num_communicates

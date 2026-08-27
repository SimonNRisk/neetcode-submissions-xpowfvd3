from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Multi source BFS
        # Each step of BFS, go through all rotten
        # Mark each neighbour as rotten, add to queue
        # Increment minute
        # Exit loop when either q is empty (no recently-rotted to add) or when have reached desired end state (rotten = num oranges)
        # If q empty, no end state, that means impossible - return -1
        num_rows = len(grid)
        num_cols = len(grid[0])
        num_fruits = 0
        rotten = []
        minutes = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] != 0:
                    num_fruits +=1
                if grid[r][c] == 2:
                    rotten.append((r, c))
        # Start BFS from rotten fruit
        q = deque(rotten)
        num_rotten = len(rotten)
        while q and num_rotten != num_fruits:
            # Loop through queue
            for _ in range(len(q)):
                # Pop each one off
                r, c = q.popleft()
                # Rot the neighbours if they are fruit
                # Up
                if r > 0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    num_rotten +=1
                    q.append((r-1, c))
                # Down
                if r < num_rows-1 and grid[r+1][c] == 1:
                    grid[r+1][c] = 2
                    num_rotten +=1
                    q.append((r+1, c))
                # Left
                if c > 0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    num_rotten +=1
                    q.append((r, c-1))
                # Right
                if c < num_cols-1 and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    num_rotten +=1
                    q.append((r, c+1))
            # At the end, incrememnt
            minutes +=1
        if num_rotten == num_fruits:
            return minutes

        return -1



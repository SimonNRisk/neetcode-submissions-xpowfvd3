class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        brute force:
        add all water cells



        find each water cell
        add to queue


        then do bfs on queue
        '''
        if not grid or not grid[0]:
            return 
        num_rows = len(grid)
        num_cols = len(grid[0])
        INF = 2147483647

        q = deque()

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        while q:
            row, col = q.popleft()
            # Up
            if row > 0 and grid[row - 1][col] == INF:
                grid[row - 1][col] = grid[row][col] + 1
                q.append((row - 1, col))

            # Down
            if row < num_rows - 1 and grid[row + 1][col] == INF:
                grid[row + 1][col] = grid[row][col] + 1
                q.append((row + 1, col))

            # Left
            if col > 0 and grid[row][col - 1] == INF:
                grid[row][col - 1] = grid[row][col] + 1
                q.append((row, col - 1))

            # Right
            if col < num_cols - 1 and grid[row][col + 1] == INF:
                grid[row][col + 1] = grid[row][col] + 1
                q.append((row, col + 1))

        return


        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def removeIslands(r, c):
            if (r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])):
                #this is a valid point
                #set it to zero, and call it recursively
                if (grid[r][c] == "1"):
                    grid[r][c] = "0"
                    removeIslands(r+1, c)
                    removeIslands(r-1, c)
                    removeIslands(r, c+1)
                    removeIslands(r, c-1)
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (grid[r][c] == "1"):
                    print("Here")
                    removeIslands(r, c)
                    count +=1
        print(grid)
        return count


        
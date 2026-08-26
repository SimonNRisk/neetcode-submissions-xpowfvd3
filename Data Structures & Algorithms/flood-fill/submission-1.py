class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        num_rows = len(image)
        num_cols = len(image[0])
        color_to_change = image[sr][sc]
        target_color = color
        seen = set()
        if target_color == color_to_change:
            return image

        def dfs(r, c):
            nonlocal color_to_change
            nonlocal target_color
            nonlocal seen
            if image[r][c] != color_to_change:
                return
            if (r, c) in seen:
                return
            image[r][c] = target_color
            seen.add((r, c))
            # call on neighbours
            # Up
            if r > 0:
                dfs(r-1, c)
            # Down
            if r < num_rows-1:
                dfs(r+1, c)
            # Left
            if c > 0:
                dfs(r, c-1)
            # Right
            if c < num_cols -1:
                dfs(r, c+1)
            return
        dfs(sr, sc)
        return image

            
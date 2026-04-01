class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])
        for row_idx in range(rows):
            last_open = cols-1
            for col_idx in range(cols-1, -1, -1):
                if boxGrid[row_idx][col_idx] == "*":
                    last_open = col_idx-1
                elif boxGrid[row_idx][col_idx] == "#":
                    if col_idx != last_open:
                        boxGrid[row_idx][last_open] = "#"
                        boxGrid[row_idx][col_idx] = "."
                    last_open -=1
        res = [["."] * rows for _ in range(cols)]

        for row_idx in range(rows):
            for col_idx in range(cols):
                res[col_idx][rows-row_idx-1] = boxGrid[row_idx][col_idx]
        return res


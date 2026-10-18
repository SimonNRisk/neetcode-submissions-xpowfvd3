class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        loop over grid
        backtrack on prefix match
        backtrack takes (index, coordinate tuple)
        check up down left right on the coordinate to see if == word[index]
        if so, call backtrack on that new coordinate with index +1
        else pop from our result
        base case is result == word when joined
        '''
        prefix = word[0]
        num_rows = len(board)
        num_cols = len(board[0])
        construct = []
        found = False
        seen = set()

        def backtrack(index, coordinates):
            nonlocal word
            nonlocal found
            nonlocal board
            nonlocal seen

            r, c = coordinates
            
            if board[r][c] != word[index]:
                return

            if index == len(word) -1:
                found = True
                return
            
            
            seen.add((r, c))

            if r > 0 and (r-1, c) not in seen:
                backtrack(index+1, (r-1, c))
            if r < num_rows - 1 and (r+1, c) not in seen:
                backtrack(index+1, (r+1, c))
            if c > 0 and (r, c-1) not in seen:
                backtrack(index+1, (r, c-1))
            if c < num_cols - 1 and (r, c+1) not in seen:
                backtrack(index+1, (r, c+1))
            # only reach here if made a mistake
            seen.remove((r, c))
            return


        for r in range(num_rows):
            for c in range(num_cols):
                backtrack(0, (r, c))
        return found
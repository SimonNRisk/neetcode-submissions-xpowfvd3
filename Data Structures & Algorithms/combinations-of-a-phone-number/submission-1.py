class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        seen set to avoid duplicates
        hashmap to represent choices from a letter

        recursive backtrack (combinations / permutations problem) receives running sum, index
        if running sum is equal to length of digits, add to result set
        else if not, loop through map [digit], adding choice, backtracking, popping choice

        '''
        result = []
        digit_to_char = {
            "2":["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        if not digits:
            return []
        def backtrack(running, index):
            if index == len(digits):
                running_str = "".join(running)
                result.append(running_str)
                return
            dig = digits[index]
            choices = digit_to_char[dig]
            for choice in choices:
                #will do string concatentation for now
                running.append(choice)
                backtrack(running, index+1)
                running.pop()
            return
        
        backtrack([], 0)
        return result
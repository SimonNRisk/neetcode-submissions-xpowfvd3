class Solution:
    def decodeString(self, s: str) -> str:
        # get string as:
        # k[encoded_string]
        # encoded string in square brackets is repeated k times
        # k is positive integer
        # input string always valid
        # stack problem
        # iterate until get to a closed bracket
        # then pop from stack (tuple)
        # add to result
        stack = []
        for char in s:
            if char == "]":
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
            else:
                stack.append(char)
        return "".join(stack)

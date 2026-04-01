class Solution:
    def isValid(self, s: str) -> bool:
        # lets say we have:
        # ([{}])
        # while opening add to array
        # once not open, iterate thru starting at index
        # popping if equal in our kvp
        pairings = {")": "(", "]": "[", "}": "{" }
        closing = set([")", "]", "}"])
        opening = set(["(", "[", "{"])

        stack = []
        for letter in s:
            if letter in opening:
                stack.append(letter)
                continue
            elif letter not in closing:
                print(f"letter not in closing, {letter}")
                return False
            elif not stack:
                print(f"elif not stack, {letter}")
                return False
            elif stack[-1] != pairings[letter]:
                print(f"{stack}, {letter}")
                return False
            stack.pop()
        return not stack
        
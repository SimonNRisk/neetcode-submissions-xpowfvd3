class Solution:
    def isValid(self, s: str) -> bool:
        #given string s
        #append opening brackets
        opens = "([{"
        closes = ")]}"
        mappy = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack_list = []
        for letter in s:
            if letter in opens:
                stack_list.append(letter)
            elif letter in closes:
                if not stack_list:
                    return False
                elif mappy[letter] != stack_list[-1]:
                    return False
                stack_list.pop()
        return not stack_list
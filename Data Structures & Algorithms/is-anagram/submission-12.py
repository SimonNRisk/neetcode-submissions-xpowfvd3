class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mappy = {}
        for letter in s:
            mappy[letter] = mappy.get(letter, 0) + 1
        for letter in t:
            if letter not in mappy:
                return False
            mappy[letter] -=1
            if mappy[letter] < 0:
                return False

        return True
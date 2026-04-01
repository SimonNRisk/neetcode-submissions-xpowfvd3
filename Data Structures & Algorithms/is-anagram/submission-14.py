class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        s_map = {}
        for letter in s:
            s_map[letter] = s_map.get(letter, 0) +1
        for letter in t:
            if s_map.get(letter, 0) == 0:
                return False
            else:
                s_map[letter] -=1
        return True
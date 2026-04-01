class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s = {}
        for letter in s:
            map_s[letter] = map_s.get(letter, 0) +1
        for letter_t in t:
            if map_s.get(letter_t, 0) == 0:
                return False  
            map_s[letter_t] -= 1
            
        return True
            
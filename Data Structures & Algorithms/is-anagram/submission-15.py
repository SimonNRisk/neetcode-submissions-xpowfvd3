class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #need to return true if they have the same letters and frequency of letters
        #cant use a set as wouldnt hold letter frequency
        #can use a dict for letter frequency, map each letter as a key and frequency as a value
        # could compare the hashmaps, but this is O(2n), instead lets build a dict from 1st, remove from 2nd. should get exactly an empty dict
        if len(s) != len(t):
            return False
        freq_map = {}
        for letter in s:
            freq_map[letter] = freq_map.get(letter, 0) +1
        for letter in t:
            if freq_map.get(letter, 0) <= 0:
                return False
            freq_map[letter] -=1
            # remove one from the freq map under this letter
            # if there is a value, remove, check if
        return True
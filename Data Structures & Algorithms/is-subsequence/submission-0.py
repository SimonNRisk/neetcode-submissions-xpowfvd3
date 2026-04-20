class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index = 0
        successes = 0
        for letter in s:
            while index < len(t):
                if letter == t[index]:
                    # we found it
                    index +=1
                    successes +=1
                    break
                else:
                    index +=1
        return successes == len(s)

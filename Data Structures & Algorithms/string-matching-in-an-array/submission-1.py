class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = []
        for word in words:
            matches = 0
            for string in words:
                if word in string:
                    matches +=1
            if matches > 1:
                substrings.append(word)
        return substrings
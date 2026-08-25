class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = []
        for word in words:
            matches = 0
            for string in words:
                if word != string and word in string:
                    substrings.append(word)
                    break
        return substrings
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        res = []
        limit = min(n1, n2)
        for i in range(limit):
            res.append(word1[i])
            res.append(word2[i])

        for i in range(limit, n1):
            res.append(word1[i])
        for i in range(limit, n2):
            res.append(word2[i])

        return "".join(res)  
        
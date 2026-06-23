class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        first, second = 0, 0
        res = []
        while first < len(word1) and second < len(word2):
            res.append(word1[first])
            res.append(word2[second])
            first +=1
            second +=1
        
        if first != len(word1):
            for i in range(first, len(word1)):
                res.append(word1[i])
        elif second != len(word2):
            for i in range(second, len(word2)):
                res.append(word2[i])

        return "".join(res)  
        
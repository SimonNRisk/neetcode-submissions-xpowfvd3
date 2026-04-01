class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        for i in range(n):
            temp = temperatures[i]
            for j in range(i+1, n):
                if temperatures[j] > temp:
                    res[i] = j-i
                    break
        return res
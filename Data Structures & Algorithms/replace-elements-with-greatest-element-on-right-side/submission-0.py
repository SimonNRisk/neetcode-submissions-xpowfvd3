class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxr=-1
        placeholder = 0
        for i in range(n-1, -1, -1):
            placeholder = maxr
            maxr = max(maxr, arr[i])
            arr[i] = placeholder
        return arr
        
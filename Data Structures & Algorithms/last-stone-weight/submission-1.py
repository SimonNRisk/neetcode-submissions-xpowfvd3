import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while (len(stones) > 1):
            maxx = heapq.heappop(stones)
            #now the second largest
            maxx2 = heapq.heappop(stones)
            if (maxx != maxx2):
                heapq.heappush(stones, maxx-maxx2)
        return -stones[0] if len(stones) > 0 else 0

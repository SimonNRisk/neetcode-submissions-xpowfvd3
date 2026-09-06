import heapq
import math
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # Max heap
        heap = [-gift for gift in gifts]
        heapq.heapify(heap)

        for _ in range(k):
            value = -heapq.heappop(heap)
            floor = math.floor(math.sqrt(value))
            heapq.heappush(heap, -floor)
        
        result = 0
        for val in heap:
            result += val
        
        return -result
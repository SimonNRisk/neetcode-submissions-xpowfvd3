import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        result = []
        for point in points:
            pyth = (point[0]**2) + point[1]**2
            heapq.heappush(distances, (pyth, point)) 
        
        while k>0 and distances:
            result.append(heapq.heappop(distances)[1])
            k-=1

        return result

              

        
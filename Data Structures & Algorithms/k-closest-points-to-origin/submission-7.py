import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        given 2d array of points
        points[i] = [xi, yi] (coordinates)
        want to return k closest points to the origin (0, 0)
        euclidean distnace
        return result in any order, guaranteed to be unique


        for each element, calculate distance
        add (distance, index) tuple to a min-heap
        once through all
        loop over k:
            pop from min heap
            add arr[index] to res
        return res
        '''
        res = []
        heap = []
        # Edge case where k > num points - what do we do there?
        if k > len(points):
            return points
        for index, point in enumerate(points):
            distance = (point[0]**2 + point[1]**2)**0.5
            tup = (distance, index)
            heapq.heappush(heap, tup)
        for i in range(k):
            distance, index = heapq.heappop(heap)
            point = points[index]
            res.append(point)
        return res









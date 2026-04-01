import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #O(n)
        nums = [-num for num in nums]
        #O(n)
        heapq.heapify(nums)
        while (nums and k>1):
            heapq.heappop(nums)
            k-=1
        return -nums[0]
        
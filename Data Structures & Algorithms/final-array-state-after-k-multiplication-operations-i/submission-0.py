import heapq
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # get array of integers
        # get an integer k
        # get an integer multiplier
        # Perform k operations
        # For each:
        # find minimum value in nums (if multiple, take first)
        # replace the selected minimum value with value * multiplier
        # return integer array after
        # min heap provides easy access to the minumum value, and would be the first minimum (O(n) to create, O(logn) to push / pop)
        # Could construct a min heap with nums
        # each operation, could pop min, modify, push back
        # main Q is how to do this without order changing?
        # works! but order changes now...
        # could you push the number and the index as a tuple to our heap?
        # then construct it, and change the array in place?
        # let's try it!
        heap = []
        for index, num in enumerate(nums):
            heapq.heappush(heap, (num, index))
        while k > 0:
            min_val, min_index = heapq.heappop(heap)
            new_val = min_val*multiplier
            nums[min_index] = new_val
            heapq.heappush(heap, (new_val, min_index))
            k -=1
        return nums

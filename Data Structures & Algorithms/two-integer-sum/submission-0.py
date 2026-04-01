class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #given array of numbers
        #target int
        #return indicies whose elements add to target
        #target - each number
        #look for that in next
        #hash, values are indicies, keys are difference
        mappy = {}
        for index, num in enumerate(nums):
            difference = target-num
            if difference in mappy:
                return [mappy[difference], index]
            mappy[num] = index

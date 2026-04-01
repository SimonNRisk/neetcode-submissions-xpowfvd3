class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # array of numbers
        # return indices that add to target
        # single option, return smaller index first
        # loop through, adding target - num to map with index as value
        # then once key in map, means 
        diff_to_index = {}
        for index, num in enumerate(nums):
            if num in diff_to_index:
                return [diff_to_index[num], index]
            diff_to_index[target-num] = index
        return -1
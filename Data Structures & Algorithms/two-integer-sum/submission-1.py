class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #want hashmap of numbers
        #if the difference is one of the numbers in our hash, we god
        mappy = {}
        for index, number in enumerate(nums):
            difference = target - number
            if difference in mappy:
                return [mappy[difference], index]
            mappy[number] = index

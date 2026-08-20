class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # nums[i] is in the range 1..n
        # return array of ints that arent in that range
        unique_nums = set(nums)
        n = len(nums)
        missing = [i for i in range(1, n+1) if i not in unique_nums]
        return missing
        
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map = {}
        n = len(nums)
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        for num in nums:
            if freq_map[num] > n //2:
                return num
        return 0

        
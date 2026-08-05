class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) == 1:
            return False
        vk = {}
        for idx, val in enumerate(nums):
            if val in vk and abs(vk[val] - idx) <= k:
                return True
            else:
                vk[val] = idx
        return False

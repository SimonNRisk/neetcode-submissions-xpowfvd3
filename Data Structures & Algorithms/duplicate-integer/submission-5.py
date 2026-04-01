class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        el_set = set()
        for num in nums:
            if num in el_set:
                return True
            else:
                el_set.add(num)
        return False
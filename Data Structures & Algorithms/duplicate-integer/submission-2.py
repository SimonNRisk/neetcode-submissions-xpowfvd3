class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         #return true if any value appears more than once
         #else return false
        #return true if duplicate
        setty = set()
        for num in nums:
            if num in setty:
                return True
            else:
                setty.add(num)
        return False
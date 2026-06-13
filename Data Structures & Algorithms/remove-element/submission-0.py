class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # given array and value
        # remove all value instances in array in-place
        # we can change order (Onlogn)
        # return # of array elements != val
        # if # array elements == val = k
        # change array so first k elements contain non-equal values
        # remaining dont matter
        # return k
        
        # one pointer to show where to insert
        # one to hunt targets
        # plan is we look for 2
        k = 0 # insertion index
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

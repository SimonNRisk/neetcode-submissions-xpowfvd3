class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        # 
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else: ## target == nums[mid]
                return mid     
        if nums[mid] > target:
            return mid
        else:
            return mid + 1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            print(mid)
            if nums[mid] == target:
                print(f"found nums[mid]")
                return mid
            if nums[mid] < target:
                print(f"found nums[mid] < target {nums[mid]}")
                left = mid + 1
            elif nums[mid] > target:
                print(f"found nums[mid] > target {nums[mid]}")
                right = mid - 1
        return -1
        
        

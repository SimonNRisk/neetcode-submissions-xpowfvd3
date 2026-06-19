class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        if num == 2:
            return False
        if num == 3:
            return False
        half = num //3
        nums = [i for i in range(half)]
        left, right = 0, half-1
        while left <= right:
            mid = (left + right) // 2  
            square = nums[mid] **2
            if square == num:
                return True
            elif square > num:
                right = mid - 1
            else:
                left = mid + 1
        return False       
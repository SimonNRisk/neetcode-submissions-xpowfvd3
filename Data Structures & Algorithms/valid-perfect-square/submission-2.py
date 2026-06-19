class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # for any number, its sqrt is between 0 and that num (positive)
        if num == 1:
            return True
        half = num //2
        nums = [i for i in range(half)]
        left, right = 0, half-1
        while left <= right:
            mid = (left + right) // 2  
            square = nums[mid] **2
            print(square)
            if square == num:
                return True
            elif square > num:
                right = mid - 1
            else:
                left = mid + 1
        return False       
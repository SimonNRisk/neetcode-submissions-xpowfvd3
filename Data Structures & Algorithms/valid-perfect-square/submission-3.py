class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt_num = int(num ** 0.5)
        perfect_square = sqrt_num * sqrt_num
        return num == perfect_square
     
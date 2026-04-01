class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        water = 0
        while left < right:
            min_height = min(heights[left], heights[right])
            area = min_height * (right-left)
            water = max(water, area)
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return water
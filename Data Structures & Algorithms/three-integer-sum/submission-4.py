class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solutions = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i>0 and nums[i-1] == nums[i]:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                threesum = num + nums[left] + nums[right]
                if threesum > 0:
                    right-=1
                elif threesum < 0:
                    left +=1
                else:
                    solutions.append([num, nums[left], nums[right]])
                    left +=1
                    right -=1
                    while nums[left] == nums[left -1] and left<right:
                        left +=1
        return solutions
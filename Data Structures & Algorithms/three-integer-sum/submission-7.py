class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            hi = n-1
            lo = i+1
            while hi > lo:
                total = nums[i] + nums[hi] + nums[lo]
                if total == 0:
                    res.append([nums[i], nums[hi], nums[lo]])
                    # move until new
                    hi -=1
                    lo +=1
                    while hi > lo and nums[hi] == nums[hi+1]:
                        hi -=1
                    while hi > lo and nums[lo] == nums[lo-1]:
                        lo +=1
                elif total > 0:
                    hi -=1
                else:
                    lo +=1
        return res
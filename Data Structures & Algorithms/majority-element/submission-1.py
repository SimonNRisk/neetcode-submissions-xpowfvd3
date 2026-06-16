class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # not the mode, but the majority element
        cur_mode = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == cur_mode:
                count += 1
            else:
                if count == 0:
                    cur_mode = nums[i]
                else:
                    count -=1
        return cur_mode


        '''
        freq_map = {}
        n = len(nums)
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        for num in nums:
            if freq_map[num] > n //2:
                return num
        return 0\
        '''

        
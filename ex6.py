class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return nums[i]
        # return 

        for i in range(len(nums)):
            while (nums[i] != i):
                if nums[i] != nums[nums[i]]:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                else:
                    return nums[i]
        return

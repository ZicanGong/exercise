class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        """
        unfinished
        """
        hindex = len(nums) - k + 1
        lindex = 0
        for i in range(len(nums)-1, -1, -1):
            curnum = nums[i]
            plnum = lnum
            psnum = snum
            if curnum >= lnum:
                if m < k:
                    m = m + 1
                else:
                    lnum = psnum if curnum > psnum else curnum
            else:
                if m < k:
                    m = m + 1
                    lnum = curnum
            if curnum <= snum:
                if n < l:
                    n = n + 1
                else:
                    snum = plnum if curnum < plnum else curnum
            else:
                if n < l:
                    n = n + 1
                    snum = curnum
        if k == len(nums):
            return lnum
        else:
            return snum
        return null

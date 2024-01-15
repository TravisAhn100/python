class Solution(object):
            
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        [1,2,2]
        """
        l=0
        s=0
        for i in  range(len(nums)):
            s=nums[i]
            while i <= len(nums)-1:
                i+=1
                if nums[i] != s:
                    l+=1
                    nums[l]=nums[i]
                    break


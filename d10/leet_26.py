class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mt_list = []
        for num in nums:
            mt_list += num
            

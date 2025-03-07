class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        num_set = set(range(n + 1))  
        for num in nums:
            num_set.discard(num)  
        return num_set.pop()

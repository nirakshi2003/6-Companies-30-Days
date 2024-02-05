class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        max_list = sorted(nums, reverse=True)[:k]
        for num in nums:
            if num in max_list:
                result.append(num)
                max_list.remove(num)
                if len(max_list) == 0:
                    return result

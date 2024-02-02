class Solution(object):
    def incremovableSubarrayCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def ss(arr):
            for i in range(len(arr)-1):
                if(arr[i]>=arr[i+1]):
                    return 0
            return 1
        p=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                temp=nums[:]
                del temp[i:j]
                if ss(temp)==1:
                    p+=1
        return p

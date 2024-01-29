class Solution(object):
    def smallestTrimmedNumbers(self, nums, queries):
        """
        :type nums: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        def trim_and_index(nums, k, trim):
            trimmed_nums = [int(num[-trim:]) for num in nums]
            trimmed_nums_with_index = [(num, i) for i, num in enumerate(trimmed_nums)]
            trimmed_nums_with_index.sort()
            kth_smallest_num = trimmed_nums_with_index[k-1][0]
            kth_smallest_index = trimmed_nums_with_index[k-1][1]
            return kth_smallest_num, kth_smallest_index

        def process_queries(queries, nums):
            result = []
            for k, trim in queries:
                kth_smallest_num, kth_smallest_index = trim_and_index(nums, k, trim)
                result.append(kth_smallest_index)
            return result

        return process_queries(queries, nums)

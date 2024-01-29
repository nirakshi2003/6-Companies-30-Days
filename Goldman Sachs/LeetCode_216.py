import itertools as it

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        all_combinations = it.combinations(range(1, 10), k)
        result = [comb for comb in all_combinations if sum(comb) == n]
        return result

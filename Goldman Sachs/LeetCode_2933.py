class Solution(object):
    def findHighAccessEmployees(self, access_times):
        """
        :type access_times: List[List[str]]
        :rtype: List[str]
        """
        sorted_access_times = sorted(access_times)
        arr = set()
        for i in range(len(sorted_access_times) - 2):
            if (int(sorted_access_times[i+2][1]) - int(sorted_access_times[i][1])) < 100 and (sorted_access_times[i+2][0] == sorted_access_times[i][0]):
                arr.add(sorted_access_times[i][0])
        return list(arr)

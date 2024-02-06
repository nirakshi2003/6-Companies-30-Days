class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        distances = []
        for r in range(rows):
            for c in range(cols):
                distances.append(([r, c], abs(r - rCenter) + abs(c - cCenter)))
        distances.sort(key=lambda x: x[1])
        result = [d[0] for d in distances]
        return result

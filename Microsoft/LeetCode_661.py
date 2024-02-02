class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        rows, cols = len(img), len(img[0])
        result = [[0] * cols for _ in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                total_pixels = 0
                total_sum = 0
                
                for x in range(max(0, i - 1), min(rows, i + 2)):
                    for y in range(max(0, j - 1), min(cols, j + 2)):
                        total_pixels += 1
                        total_sum += img[x][y]
                
                result[i][j] = total_sum // total_pixels
        
        return result

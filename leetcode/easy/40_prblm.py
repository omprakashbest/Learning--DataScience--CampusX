"""
-> Image Smoother

An image smoother is a filter of the size 3x3 that can be applied to each of an image by rounding down the average
of the cell and the eight surrounding cells (i.e, the average of the nine cells in the blue smoother). if one or
more of the surrounding cells of a cells is not present, we do not consider it in the average (i.e, the average of
the four cells in the red smoother).

Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the 
smoother on each cell of it.

"""

class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        ROWS, COLS = len(img), len(img[0])

        res = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                total, count = 0, 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if i < 0 or i == ROWS or j < 0 or j == COLS:
                            continue
                        total += img[i][j]
                        count += 1
                res[r][c] = total // count
        return res

obj = Solution()
img = [[1,1,1],[1,0,1],[1,1,1]]
print(obj.imageSmoother(img))
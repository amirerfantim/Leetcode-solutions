from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        res = 0
        size = len(mat)

        for i in range(size):
            res += mat[i][i]

            if i != size - i - 1:
                res += mat[i][size - i - 1]

        return res

s1 = Solution()
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
print(s1.diagonalSum(mat))


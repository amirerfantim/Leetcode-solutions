from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        new_mat = []
        temp = []

        for row in mat:
            for num in row:
                temp.append(num)

        if len(temp) != r * c:
            return mat

        for i in range(0, len(temp), c):
            new_mat.append(temp[i:i + c])

        return new_mat


s1 = Solution()
mat = [[1, 2], [3, 4]]
r = 1
c = 4
print(s1.matrixReshape(mat, r, c))

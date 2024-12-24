from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix[row])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in range(len(matrix)):
            matrix[row] = matrix[row][::-1]


s1 = Solution()
print(s1.rotate([[1,2,3],[4,5,6],[7,8,9]]))
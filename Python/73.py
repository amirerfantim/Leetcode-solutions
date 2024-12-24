from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_columns = set()
        zero_rows = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    zero_columns.add(col)
                    zero_rows.add(row)

        for col in zero_columns:
            for row in range(len(matrix)):
                matrix[row][col] = 0

        for row in zero_rows:
            for col in range(len(matrix[row])):
                matrix[row][col] = 0

        print(matrix)


s1 = Solution()
print(s1.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))

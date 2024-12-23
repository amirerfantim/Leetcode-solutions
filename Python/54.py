from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        vertical_direction = 0
        horizontal_direction = 1
        matrix_size = len(matrix) * len(matrix[0])
        row = 0
        col = 0
        result = []
        while True:
            if len(result) == matrix_size:
                return result
            if horizontal_direction == 1:
                while col < len(matrix[row]) and matrix[row][col] is not None:
                    result.append(matrix[row][col])
                    matrix[row][col] = None
                    col += 1
                horizontal_direction = 0
                vertical_direction = -1
                col -= 1
                row += 1

            if vertical_direction == -1:
                while row < len(matrix) and matrix[row][col] is not None:
                    result.append(matrix[row][col])
                    matrix[row][col] = None
                    row += 1
                horizontal_direction = -1
                vertical_direction = 0
                row -= 1
                col -= 1

            if horizontal_direction == -1:
                while col >= 0 and matrix[row][col] is not None:
                    result.append(matrix[row][col])
                    matrix[row][col] = None
                    col -= 1
                horizontal_direction = 0
                vertical_direction = 1
                row -= 1
                col += 1

            if vertical_direction == 1:
                while row < len(matrix) and matrix[row][col] is not None:
                    result.append(matrix[row][col])
                    matrix[row][col] = None
                    row -= 1
                horizontal_direction = 1
                vertical_direction = 0
                row += 1
                col += 1


s1 = Solution()
print(s1.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))

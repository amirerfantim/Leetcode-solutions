from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def search(left, right):
            if left > right:
                return False

            mid = (right + left) // 2
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                return search(mid + 1, right)
            elif target < matrix[row][col]:
                return search(left, mid - 1)
        return search(0, len(matrix) * len(matrix[0]) - 1)


s1 = Solution()
print(s1.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1))

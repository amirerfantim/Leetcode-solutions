from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            count = 0
            mid = (left + right) // 2
            j = n - 1
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                count += j + 1
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left


s1 = Solution()
print(s1.kthSmallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 6))

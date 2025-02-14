from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows, cols = {}, {}
        res = 0
        for row in grid:
            row = str(row)
            if row not in rows:
                rows[row] = 1
            else:
                rows[row] += 1

        for i in range(len(grid[0])):
            current_col = []
            for j in range(len(grid)):
                current_col.append(grid[j][i])
            current_col = str(current_col)
            if current_col in rows:
                res += rows[current_col]

        return res


s1 = Solution()
print(s1.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))

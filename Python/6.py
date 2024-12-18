class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        current_row = 0
        getting_down = False

        for char in s:
            rows[current_row].append(char)
            if current_row == numRows - 1:
                getting_down = True
                current_row -= 1
            elif current_row == 0:
                getting_down = False
                current_row += 1
            elif getting_down:
                current_row -= 1
            else:
                getting_down = False
                current_row += 1

        return "".join(''.join(row) for row in rows)


s1 = Solution()
print(s1.convert("PAYPALISHIRING", 3))

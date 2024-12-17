class Solution:
    def romanToInt(self, s: str) -> int:
        index = 0
        integer = 0
        while index < len(s):
            if s[index] == 'I':
                if index + 1 < len(s) and s[index + 1] == 'V':
                    integer += 4
                    index += 1
                elif index + 1 < len(s) and s[index + 1] == 'X':
                    integer += 9
                    index += 1
                else:
                    integer += 1
            elif s[index] == 'V':
                integer += 5
            elif s[index] == 'X':
                if index + 1 < len(s) and s[index + 1] == 'L':
                    integer += 40
                    index += 1
                elif index + 1 < len(s) and s[index + 1] == 'C':
                    integer += 90
                    index += 1
                else:
                    integer += 10
            elif s[index] == 'L':
                integer += 50
            elif s[index] == 'C':
                if index + 1 < len(s) and s[index + 1] == 'D':
                    integer += 400
                    index += 1
                elif index + 1 < len(s) and s[index + 1] == 'M':
                    integer += 900
                    index += 1
                else:
                    integer += 100
            elif s[index] == 'D':
                integer += 500
            elif s[index] == 'M':
                integer += 1000
            index += 1
        return integer

s = Solution()
print(s.romanToInt("MCMXCIV"))
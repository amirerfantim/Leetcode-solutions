class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_divisor(l):
            if len(str1) % l or len(str2) % l:
                return False
            factor1 = len(str1) // l
            factor2 = len(str2) // l
            return (factor1 * str1[:l] == str1) and (factor2 * str2[:l] == str2)

        for i in range(min(len(str1), len(str2)), 0, -1):
            if is_divisor(i):
                return str1[:i]


s1 = Solution()
print(s1.gcdOfStrings("ababab", 'abc'))

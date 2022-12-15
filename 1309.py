class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ''
        i = 0
        while i < len(s):
            if '#' in s[i:i + 3]:
                res += chr(96 + int(s[i:i + 2]))
                i += 3
            else:
                res += chr(96 + int(s[i:i + 1]))
                i +=1
        return res


s1 = Solution()
print(s1.freqAlphabets("10#11#12"))

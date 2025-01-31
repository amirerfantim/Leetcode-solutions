class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        res_len = 0


        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > res_len:
                    res_len = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1

        for i in range(len(s) - 1):
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > res_len:
                    res_len = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1
        return res


s1 = Solution()
print(s1.longestPalindrome("babad"))

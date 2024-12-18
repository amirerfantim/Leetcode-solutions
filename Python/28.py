class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)
        for i in range(len(haystack) - needle_len + 1):
            if haystack[i:i + needle_len] == needle:
                return i
        return -1


s1 = Solution()
print(s1.strStr("mississippi", "issip"))

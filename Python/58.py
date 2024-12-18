class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1]) if words else 0


s1 = Solution()
print(s1.lengthOfLastWord("hello world"))
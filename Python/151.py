class Solution(object):
    def reverseWords(self, s):
        return ' '.join(reversed(s.split()))



s1 = Solution()
s = "the sky    is blue   "
print(s1.reverseWords(s))
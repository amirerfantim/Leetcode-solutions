from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = Counter(s)
        counter_t = Counter(t)
        return counter_s == counter_t



s1 = Solution()
s = "a"
t = "ab"
print(s1.isAnagram(s, t))

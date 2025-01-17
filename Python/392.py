class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_index = 0
        t_index = 0
        while s_index < len(s) and t_index < len(t):
            if s[s_index] == t[t_index]:
                s_index += 1
                t_index += 1
            elif s[s_index] != t[t_index]:
                t_index += 1
        if s_index == len(s):
            return True
        return False


s1 = Solution()
s = "acb"
t = "ahbgdc"
print(s1.isSubsequence(s, t))

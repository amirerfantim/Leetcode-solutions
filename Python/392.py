class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        cur_index = -1
        for char_s in s:
            if char_s in t[cur_index + 1:]:
                new_index = t[cur_index+1:].index(char_s)
                cur_index = cur_index + new_index + 1
                # new = t[:cur_index] + t[cur_index+1:]
                # t = new
            else:
                return False
        return True


s1 = Solution()
s = "aaa"
t = "bbaaaa"
print(s1.isSubsequence(s, t))

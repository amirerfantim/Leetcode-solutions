class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur_sub = []
        max_len = 0
        cur_len = 0
        for i in range(len(s)):

            if s[i] not in cur_sub:
                cur_len += 1
                cur_sub.append(s[i])
            else:
                index = cur_sub.index(s[i])
                cur_sub = cur_sub[index + 1:]
                cur_sub.append(s[i])
                cur_len = len(cur_sub)
            if cur_len > max_len:
                max_len = cur_len
        return max_len


s1 = Solution()
s = " "
print(s1.lengthOfLongestSubstring(s))

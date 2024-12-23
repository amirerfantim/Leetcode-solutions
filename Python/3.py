from logging import currentframe


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            current_length = right - left + 1
            if current_length > max_length:
                max_length = current_length
            char_set.add(s[right])
        return max_length

s1 = Solution()
s = "bbbbb"
print(s1.lengthOfLongestSubstring(s))

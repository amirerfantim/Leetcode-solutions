from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        char_index = 0
        min_len = float('inf')
        for index in range(len(strs)):
            if len(strs[index]) < min_len:
                min_len = len(strs[index])
        while char_index < min_len:
            current_char = strs[0][char_index]
            flag = False
            for i in range(1, len(strs)):
                if current_char != strs[i][char_index]:
                    flag = True
                    break
            if flag:
                break
            prefix = prefix + current_char
            char_index = char_index + 1
        return prefix


s1 = Solution()
print(s1.longestCommonPrefix(["dog","racecar","car"]))

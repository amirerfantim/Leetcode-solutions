from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        group_len = 0
        cur_index = 0
        cur_letter = chars[0]
        chars.append('!')
        for i in range(len(chars)):
            if chars[i] == cur_letter:
                group_len += 1
            else:
                chars[cur_index] = cur_letter
                cur_letter = chars[i]
                cur_index += 1
                if group_len > 1:
                    group_str = str(group_len)
                    for digit in group_str:
                        chars[cur_index] = digit
                        cur_index += 1
                group_len = 1
        return cur_index



s = Solution()
chars = ["a", "a", "b", "b", "c", "c", "c"]
print(s.compress(chars))

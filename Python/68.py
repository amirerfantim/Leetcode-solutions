from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, current_line, current_chars = [], [], 0
        for word in words:
            if current_chars + len(word) + len(current_line) > maxWidth:
                for i in range(maxWidth - current_chars):
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                result.append(''.join(current_line))
                current_line, current_chars = [], 0
            current_chars += len(word)
            current_line.append(word)

        for i in range(maxWidth - current_chars - len(current_line) + 1):
            current_line[-1] += " "
        result.append(' '.join(current_line))
        return result


s1 = Solution()
print(s1.fullJustify(["What","must","be","acknowledgment","shall","be"], maxWidth = 16))
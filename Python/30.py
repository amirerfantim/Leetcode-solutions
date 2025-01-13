import copy
from collections import defaultdict
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        num_words = len(words)
        s_len = len(s)

        word_count = defaultdict(int)
        for word in words:
            word_count[word] += 1

        result = []

        for i in range(word_len):
            left = i
            count = 0
            current_count = defaultdict(int)

            for j in range(i, s_len - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_count:
                    current_count[word] += 1
                    count += 1

                    while current_count[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        current_count[left_word] -= 1
                        count -= 1
                        left += word_len

                    if count == num_words:
                        result.append(left)
                else:
                    current_count.clear()
                    count = 0
                    left = j + word_len

        return result


s1 = Solution()
print(s1.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"]))

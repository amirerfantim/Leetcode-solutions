from collections import defaultdict, Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_dict = Counter(arr)
        value_set = set(freq_dict.values())
        return len(value_set) == len(freq_dict.values())


s1 = Solution()
print(s1.uniqueOccurrences([1, 2, 2, 2, 1, 1, 3]))

from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h_index = 0
        for index in range(len(citations)):
            if citations[index] < index + 1:
                h_index = index
                break
        return h_index


s1 = Solution()
print(s1.hIndex(citations=[1,3,1]))

from collections import defaultdict
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        index = 0
        while index < len(nums):
            start = nums[index]
            while index < len(nums) - 1 and nums[index + 1] - nums[index] == 1:
                index += 1
            end = nums[index]
            if start == end:
                result.append(str(start))
            else:
                result.append(str(start) + '->' + str(end))
            index += 1
        return result


s1 = Solution()
print(s1.summaryRanges([0, 1, 2, 4, 5, 7]))

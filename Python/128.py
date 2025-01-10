from collections import defaultdict
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in nums_set:
                    current_streak += 1
                    current_num += 1
                longest = max(longest, current_streak)
        return longest


s1 = Solution()
print(s1.longestConsecutive([100,4,200,1,3,2]))

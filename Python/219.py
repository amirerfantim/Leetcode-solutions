from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        recurrence = {}
        for i in range(len(nums)):
            if nums[i] in recurrence and  i - recurrence[nums[i]] <= k:
                return True
            else:
                recurrence[nums[i]] = i
        return False


s1 = Solution()
print(s1.containsNearbyDuplicate([1,0,1,1], 1))
from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        res = 0

        while l < r:
            current = nums[l] + nums[r]
            if current < k:
                l += 1
            elif current > k:
                r -= 1
            else:
                r -= 1
                l += 1
                res += 1
        return res


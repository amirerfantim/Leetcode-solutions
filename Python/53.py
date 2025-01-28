from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result = nums[0]
        current = nums[0]

        for num in range(nums[1:]):
            current = max(num, current + num)
            result = max(result, current)


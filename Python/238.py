from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        for index in range(1, len(nums)):
            result[index] = result[index - 1] * nums[index - 1]

        multiplier = 1
        for reversed_index in range(len(nums) - 2, -1, -1):
            multiplier *= nums[reversed_index + 1]
            result[reversed_index] = result[reversed_index] * multiplier


s1 = Solution()
s1.productExceptSelf(nums=[-1,1,0,-3,3])


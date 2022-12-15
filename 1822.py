from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        for num in nums:
            if num < 0:
                result *= -1
            elif num == 0:
                return 0
        return result


s1 = Solution()
nums = [-1, -2, -3, -4, 3, 2, 1]
print(s1.arraySign(nums))
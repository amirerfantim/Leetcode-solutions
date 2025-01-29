from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        current_max, current_min = 1, 1

        for num in nums:
            temp = current_max * num
            current_max = max(temp, num, current_min * num)
            current_min = min(temp, num, current_min * num)
            res = max(res, current_max)
        return res


s1 = Solution()
print(s1.maxProduct([2, 3, -2, 4]))

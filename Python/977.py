from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        res = []
        while start <= end:
            if abs(nums[start]) >= abs(nums[end]):
                res.append(nums[start] * nums[start])
                start += 1
            else:
                res.append(nums[end] * nums[end])
                end -= 1
        res.reverse()
        return res


s1 = Solution()
nums = [-4, -1, 0, 3, 10]
print(s1.sortedSquares(nums))

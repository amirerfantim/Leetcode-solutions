from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums)
        k = k % length
        nums = nums[length - k:] + nums[:length - k]
        print(nums)


s1 = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
s1.rotate(nums, 3)

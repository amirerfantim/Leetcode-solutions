from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_pointer = 0
        for main_pointer in range(len(nums)):
            if nums[main_pointer] != 0:
                nums[main_pointer], nums[zero_pointer] = nums[zero_pointer], nums[main_pointer]
                zero_pointer += 1


s1 = Solution()
nums = [0, 1, 0, 3, 12]
s1.moveZeroes(nums)

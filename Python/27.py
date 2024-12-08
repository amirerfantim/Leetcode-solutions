from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        left = 0
        while left < len(nums) - counter:
            if nums[left] == val:
                nums[left] = nums[len(nums) - 1 - counter]
                counter += 1
            else:
                left += 1
        return len(nums) - counter

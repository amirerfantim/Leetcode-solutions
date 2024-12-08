from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_idx = 1
        for org_idx in range(len(nums) - 1):
            if nums[org_idx] != nums[org_idx + 1]:
                nums[unique_idx] = nums[org_idx + 1]
                unique_idx += 1
        if len(nums) == 0:
            return 0
        return unique_idx


s1 = Solution()
s1.removeDuplicates([1, 1, 1, 2, 2, 3])
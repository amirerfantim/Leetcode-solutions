from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_idx = 2
        if len(nums) <= 2:
            return 2
        for org_idx in range(2, len(nums)):
            if nums[unique_idx - 2] != nums[org_idx]:
                nums[unique_idx] = nums[org_idx]
                unique_idx += 1
        return unique_idx


s1 = Solution()
s1.removeDuplicates([0,0,1,1,1,1,2,3,3])
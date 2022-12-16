from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for x, y in zip(nums[:-1], nums[1:]):
            if x == y:
                return True
        return False


s1 = Solution()
nums = [1, 2, 3, 4]
print(s1.containsDuplicate(nums))

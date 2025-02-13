from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        sp = 0
        res = 0
        current_zeros = 0
        for fp in range(len(nums)):
            if nums[fp] == 0:
                current_zeros += 1
            while current_zeros > k:
                if nums[sp] == 0:
                    current_zeros -= 1
                sp += 1
            if fp - sp + 1 > res:
                res = fp - sp + 1
        return res


s1 = Solution()
print(s1.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))

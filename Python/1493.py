from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        flag = False
        sp = 0
        res = 0
        for fp in range(len(nums)):
            if nums[fp] == 0:
                if not flag:
                    flag = True
                else:
                    while flag:
                        if nums[sp] == 0:
                            flag = False
                        sp += 1
                    flag = True

            if fp - sp > res:
                res = fp - sp
        return res

s1 = Solution()
print(s1.longestSubarray([1,1,0, 1]))
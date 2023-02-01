from typing import List


class Solution(object):
    def moveZeroes(self, nums):

        zero = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero.append(i)
        for j in range(len(zero)):
            nums.append(nums.pop(zero[j] - j))


s1 = Solution()
nums = [0, 1, 0, 3, 12]
print(s1.moveZeroes(nums))

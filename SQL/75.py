from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counting = [0 for _ in range(3)]

        for num in nums:
            counting[num] += 1

        for i in range(1, len(counting)):
            counting[i] += counting[i - 1]

        for i in range(len(counting) - 1, -1, -1):
            while counting[i] > 0:
                counting[i] -= 1
                nums[counting[i]] = i


        print(nums)

s1 = Solution()
s1.sortColors([2, 0, 2, 2])

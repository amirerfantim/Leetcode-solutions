from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        nums.reverse()

        for i in range(len(nums)-2):
            if nums[i] < (nums[i+1] + nums[i+2]):
                return nums[i] + nums[i+1] + nums[i+2]
        return 0


s1 = Solution()
a = [1, 2, 1, 10]
print(s1.largestPerimeter(a))

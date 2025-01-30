from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = num + nums[left] + nums[right]
                if total == 0:
                    result.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result


s1 = Solution()
print(s1.threeSum([0,0,0,0]))

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            if target - nums[i] in dictionary:
                return [dictionary[target - nums[i]], i]
            else:
                dictionary[nums[i]] = i


s1 = Solution()
print(s1.twoSum([2, 7, 11, 15], 9))
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        triple = [nums[0]]
        smaller = +999999999
        for i in range(1, len(nums)):

            if nums[i] > triple[-1]:
                triple.append(nums[i])
            if nums[i] > smaller:
                triple[0] = smaller
                if len(triple) > 1:
                    triple[1] = nums[i]
                else:
                    triple.append(nums[i])
            elif triple[-1] > nums[i] > triple[0]:
                triple[1] = nums[i]
            elif triple[-1] > nums[i] < triple[0]:
                smaller = nums[i]

            if len(triple) == 3:
                return True
        return False

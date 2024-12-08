from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def rec(nums, target, left, right, min_dis, res):
            mid = (left + right) // 2
            if left > right:
                return res
            if target > nums[mid]:
                if (target - nums[mid]) < min_dis:
                    min_dis = target - nums[mid]
                    res = mid + 1
                return rec(nums, target, mid + 1, right, min_dis, res)
            elif target == nums[mid]:
                return mid
            else:
                if (nums[mid] - target) < min_dis:
                    min_dis = nums[mid] - target
                    res = mid
                return rec(nums, target, left, mid - 1, min_dis, res)

        return rec(nums, target, 0, len(nums) - 1, 1e9, -1)


s1 = Solution()
nums = [1, 3]
target = 5

print(s1.searchInsert(nums, target))

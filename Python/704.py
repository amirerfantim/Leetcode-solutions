from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search(nums, left, right, target):
            if left <= right:
                mid = (right + left) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return search(nums, mid + 1, right, target)
                else:
                    return search(nums, left, mid - 1, target)
            return -1

        return search(nums, 0, len(nums) - 1, target)


s1 = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 0
print(s1.search(nums, target))

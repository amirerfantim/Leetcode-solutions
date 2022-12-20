from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r, arr, number):
            if l > r:
                return -1
            med = (r + l) // 2
            if number > arr[med]:
                return binary_search(med + 1, r, arr, number)
            elif number == arr[med]:
                return med
            else:
                return binary_search(l, med - 1, arr, number)

        return binary_search(0, len(nums) - 1, nums, target)


s1 = Solution()
nums = [5]
target = 5
print(s1.search(nums, target))

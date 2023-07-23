from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sorted_nums = nums.sort(reverse=True)
        return nums[k-1]

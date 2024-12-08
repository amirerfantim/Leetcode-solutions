from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current_index = 0
        while current_index < len(nums):
            max_possible_new_index = current_index + nums[current_index]
            best_new_index = current_index
            for inner_index in range(current_index, current_index + nums[current_index] + 1):
                if inner_index + nums[inner_index] > max_possible_new_index:
                    max_possible_new_index = inner_index + nums[inner_index]
                    best_new_index = inner_index
                if max_possible_new_index >= len(nums) - 1:
                    return True
            if best_new_index == current_index:
                return False
            current_index = best_new_index


s1 = Solution()
print(s1.canJump([2,0,1,0,1]))
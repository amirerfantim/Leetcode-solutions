from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        current_index = 0
        jump_steps = 0
        max_possible_new_index = current_index + nums[current_index]
        new_best_index = current_index
        if len(nums) == 1:
            return 0
        if max_possible_new_index >= len(nums) - 1:
            return 1
        while current_index < len(nums):
            for inner_index in range(current_index, min(current_index + nums[current_index] + 1, len(nums))):
                if inner_index + nums[inner_index] > max_possible_new_index:
                    max_possible_new_index = inner_index + nums[inner_index]
                    new_best_index = inner_index
            if new_best_index != current_index:
                jump_steps += 1
            if max_possible_new_index >= len(nums) - 1:
                return jump_steps + 1
            current_index = new_best_index


s1 = Solution()
print(s1.jump([1, 2]))

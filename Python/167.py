from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left  = 0
        right = len(numbers) - 1
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1

        return []


s1 = Solution()
numbers = [2,3,4]
target = 6
print(s1.twoSum(numbers, target))

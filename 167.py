from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        res = []
        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum > target:
                right -= 1
            elif cur_sum == target:
                res = [left + 1, right + 1]
                break
            else:
                left += 1
        return res


s1 = Solution()
numbers = [2, 7, 11, 15]
target = 9
print(s1.twoSum(numbers, target))

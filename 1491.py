from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary) - min(salary) - max(salary)) / (len(salary)-2)


salary = [110, 400, 250]
s1 = Solution()
print(s1.average(salary))

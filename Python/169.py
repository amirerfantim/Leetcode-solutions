import operator
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        population = {}

        for num in nums:
            if num not in population:
                population[num] = 1
            else:
                population[num] += 1

        popular = None
        maximum = 0
        for key, value in population.items():
            if value > maximum:
                maximum = value
                popular = key
        return popular

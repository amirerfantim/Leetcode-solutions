from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start_station = 0
        total_gas_cost_diff = 0
        for index in range(len(gas)):
            total_gas_cost_diff += gas[index] - cost[index]
            if total_gas_cost_diff < 0:
                start_station = index + 1
                total_gas_cost_diff = 0

        return start_station


s1 = Solution()
print(s1.canCompleteCircuit([5,1,2,3,4], [4,4,1,5,1]))

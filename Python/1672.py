from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        most_money = 0

        for person in accounts:
            sum_accounts = sum(person)
            if sum_accounts > most_money:
                most_money = sum_accounts
        return most_money


s1 = Solution()
accounts = [[1, 2, 3], [3, 2, 1]]
print(s1.maximumWealth(accounts))

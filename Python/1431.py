class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maximum = 0
        res = []
        for candy in candies:
            maximum = max(maximum, candy)
        for candy in candies:
            res.append(candy + extraCandies >= maximum)
        return res
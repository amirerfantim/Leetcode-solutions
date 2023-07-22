class Solution(object):
    def largestAltitude(self, gain):
        maximum = 0
        cur = 0
        for g in gain:
            cur += g
            if g > maximum:
                maximum = g
        return maximum
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:

    class Solution:
        def guessNumber(self, n: int) -> int:
            left = 0
            right = n

            while True:
                mid = (left + right) // 2
                cur_res = guess(mid)
                if cur_res == 0:
                    return mid
                elif cur_res == -1:
                    right = mid - 1
                else:
                    left = mid + 1





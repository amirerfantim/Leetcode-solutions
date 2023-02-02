class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        res = ''
        for i in range(len(arr)):
            arr[i] = arr[i][::-1]
            res += (arr[i] + ' ')

        return res[:-1]



s1 = Solution()
s = "Let's take LeetCode contest"
print(s1.reverseWords(s))

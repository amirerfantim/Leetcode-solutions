class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        list_s = []
        for i in s:
            list_s.append(i)
        for i in t:
            try:
                list_s.pop(list_s.index(i))
            except:
                return i


s1 = Solution()
s = "abcd"
t = "abcde"
print(s1.findTheDifference(s, t))

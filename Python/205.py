class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        string_map = {}

        for i in range(len(s)):
            if s[i] not in string_map:
                if t[i] in string_map.values():
                    return False
                string_map[s[i]] = t[i]
            else:
                if string_map[s[i]] != t[i]:
                    return False
        return True


s1 = Solution()
print(s1.isIsomorphic("cadc","baba"))
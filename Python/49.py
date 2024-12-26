from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for s in strs:
            sorted_string = ''.join(sorted(s))
            if sorted_string not in dictionary:
                dictionary[sorted_string] = [s]
            else:
                dictionary[sorted_string].append(s)
        return list(dictionary.values())



s1 = Solution()
print(s1.groupAnagrams(["","b",""]))
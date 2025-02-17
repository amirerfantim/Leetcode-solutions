class Solution:
    def reverseVowels(self, s: str) -> str:
        left, right = 0, len(s) - 1
        vowels = set('AEIOUaeiou')
        char_arr = list(s)

        while left < right:
            left_status = char_arr[left] in vowels
            right_status = char_arr[right] in vowels
            if left_status and right_status:
                char_arr[left], char_arr[right] = char_arr[right], char_arr[left]
                left += 1
                right -= 1
            elif not right_status:
                right -= 1
            elif not left_status:
                left += 1
        return ''.join(char_arr)


s1 = Solution()
print(s1.reverseVowels("IceCreAm"))

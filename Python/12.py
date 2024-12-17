class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        while num - 1000 >= 0:
            num -= 1000
            roman += "M"
        while num - 900 >= 0:
            num -= 900
            roman += "CM"
        while num - 500 >= 0:
            num -= 500
            roman += "D"
        while num - 400 >= 0:
            num -= 400
            roman += "CD"
        while num - 100 >= 0:
            num -= 100
            roman += "C"
        while num - 90 >= 0:
            num -= 90
            roman += "XC"
        while num - 50 >= 0:
            num -= 50
            roman += "L"
        while num - 40 >= 0:
            num -= 40
            roman += "XL"
        while num - 10 >= 0:
            num -= 10
            roman += "X"
        while num - 9 >= 0:
            num -= 9
            roman += "IX"
        while num - 5 >= 0:
            num -= 5
            roman += "V"
        while num - 4 >= 0:
            num -= 4
            roman += "IV"
        while num - 1 >= 0:
            num -= 1
            roman += "I"
        return roman


s1 = Solution()
print(s1.intToRoman(58))

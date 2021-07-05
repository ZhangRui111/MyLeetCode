"""
tag: 哈希表，数学，字符串
12. 整数转罗马数字
https://leetcode-cn.com/problems/integer-to-roman/
"""


class Solution1:
    """ My solution """
    def intToRoman(self, num: int) -> str:
        n_m = num // 1000
        n_d = (num % 1000) // 500
        n_c = (num % 500) // 100
        n_l = (num % 100) // 50
        n_x = (num % 50) // 10
        n_v = (num % 10) // 5
        n_i = num % 5
        res = ""
        res = res + 'M' * n_m
        res = res + 'D' * n_d
        res = res + 'C' * n_c
        res = res + 'L' * n_l
        res = res + 'X' * n_x
        res = res + 'V' * n_v
        res = res + 'I' * n_i

        res = res.replace("VIIII", "IX")
        res = res.replace("IIII", "IV")
        res = res.replace("LXXXX", "XC")
        res = res.replace("XXXX", "XL")
        res = res.replace("DCCCC", "CM")
        res = res.replace("CCCC", "CD")

        return res

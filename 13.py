"""
tag: 哈希表，数学，字符串
13. 罗马数字转整数
https://leetcode-cn.com/problems/roman-to-integer/
"""


class Solution1:
    """ My solution """
    def romanToInt(self, s: str) -> int:
        pairs = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        s = s.replace("IX", "VIIII")
        s = s.replace("IV", "IIII")
        s = s.replace("XC", "LXXXX")
        s = s.replace("XL", "XXXX")
        s = s.replace("CM", "DCCCC")
        s = s.replace("CD", "CCCC")

        res = 0
        for i in s:
            res += pairs[i]

        return res


class Solution2:
    """ Without string replacement """
    def romanToInt(self, s: str) -> int:
        pairs = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res = 0
        n_s = len(s)
        for i in range(n_s-1):
            if pairs[s[i]] < pairs[s[i+1]]:
                res -= pairs[s[i]]
            else:
                res += pairs[s[i]]
        res += pairs[s[-1]]

        return res

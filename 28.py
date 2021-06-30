"""
tag: 双指针；字符串匹配
28. 实现 strStr()
https://leetcode-cn.com/problems/implement-strstr/
"""


class Solution1:
    """ BF """
    def strStr(self, haystack: str, needle: str) -> int:
        halen = len(haystack)
        nelen = len(needle)
        if halen < nelen:
            return -1
        if nelen == 0:
            return 0

        for i in range(halen - nelen + 1):
            for j in range(nelen):
                if haystack[i] == needle[j]:
                    i += 1
                else:
                    break
                if j == nelen - 1:
                    return i - nelen

        return -1


class Solution2:
    """ BM """
    def strStr(self, haystack: str, needle: str) -> int:
        haylen = len(haystack)
        needlen = len(needle)
        return self.bm(haystack, haylen, needle, needlen)

    def badChar(self, b, m):
        """ 存储模式串的哈希表，用来快速求坏字符规则下移动位数 """
        # 初始化
        bc = list()
        for i in range(256):
            bc.append(-1)
        # m代表模式串的长度，如果有两个a, 则后面那个会覆盖前面那个
        for i in range(m):
            ascii_code = ord(b[i])
            bc[ascii_code] = i
        return bc

    def goodSuffix(self, b, m):
        """ 后缀子串和前缀子串匹配表，用来求好后缀规则下的移动位数 """
        # 初始化
        suffix, prefix = list(), list()
        for i in range(m):
            suffix.append(-1)
            prefix.append(False)

        for i in range(m - 1):
            j = i
            k = 0
            while j >= 0 and b[j] == b[m - 1 - k]:
                j -= 1
                k += 1
                suffix[k] = j + 1
            if j == -1:
                prefix[k] = True
        return suffix, prefix

    def move(self, j, m, suffix_index, ispre):
        k = m - 1 - j  # 计算好后缀长度，j代表坏字符的下标
        # 如果含有长度为 k 的好后缀，返回移动位数，
        if suffix_index[k] != -1:
            return j - suffix_index[k] + 1
        # 找头部为好后缀子串的最大长度，从长度最大的子串开始
        for r in range(j + 2, m):
            # 如果是头部
            if ispre[m - r] is True:
                return r
        # 如果没有发现好后缀匹配的串，或者头部为好后缀子串，则移动到m位，也就是匹配串的长度
        return m

    def bm(self, a, n, b, m):
        bc = self.badChar(b, m)
        suffix_index, ispre = self.goodSuffix(b, m)
        i = 0  # 第一个匹配字符
        while i <= (n - m):  # 注意结束条件
            j = m - 1
            # 从后往前匹配，匹配失败，找到坏字符
            while j >= 0:
                if a[i + j] != b[j]:
                    break
                j -= 1
            # 模式串遍历完毕，匹配成功
            if j < 0:
                return i

            # 下面为匹配失败时，如何处理
            # 求出坏字符规则下移动的位数，就是我们坏字符下标减去最靠后匹配坏字符的下标
            x = j - bc[ord(a[i + j])]
            # 好后缀情况，求出好后缀情况下的移动位数,如果不含有好后缀的话，则按照坏字符来
            y = 0
            if y < m - 1 and m - 1 - j > 0:
                y = self.move(j, m, suffix_index, ispre)
            # 移动：综合两规则取最大值
            i = i + max(x, y)

        return -1


class Solution3:
    """ KMP """
    def strStr(self, haystack: str, needle: str) -> int:
        haylen = len(haystack)
        needlen = len(needle)
        if haylen < needlen:
            return -1
        if needlen == 0:
            return 0
        return self.kmp(haystack, haylen, needle, needlen)

    def next(self, b, m):
        """ next数组，用于获取移动位数 """
        next_arr = [None] * m
        next_arr[0] = -1
        k = -1
        for i in range(1, m):
            # 我们此时知道了 [0,i-1]的最长前后缀，但是k+1的指向的值和i不相同时，我们则需要回溯
            # 因为 next[k]就时用来记录子串的最长公共前后缀的尾坐标（即长度）
            # 就要找 k+1前一个元素在next数组里的值,即next[k+1]
            while k != -1 and b[k + 1] != b[i]:
                k = next_arr[k]
            # 相同情况，就是 k的下一位，和 i 相同时，此时我们已经知道 [0,i-1]的最长前后缀
            # 然后 k - 1 又和 i 相同，最长前后缀加1，即可
            if b[k + 1] == b[i]:
                k += 1
            next_arr[i] = k
        return next_arr

    def kmp(self, a, n, b, m):
        # 获取next 数组
        next_arr = self.next(b, m)
        j = 0
        for i in range(n):
            # 发现不匹配的字符，然后根据 next 数组移动指针，移动到
            # 最大公共前后缀的，前缀的后一位
            while j > 0 and a[i] != b[j]:
                j = next_arr[j - 1] + 1
                # 超出长度
                if i > n - m + j:
                    return -1
            # 如果相同就将指针同时后移一下，比较下个字符
            if a[i] == b[j]:
                j += 1
            # 遍历完整个模式串，返回模式串的起点下标
            if j == m:
                return i - m + 1
        return -1

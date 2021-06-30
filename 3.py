"""
tag: 哈希表；字符串；滑动窗口
3. 无重复字符的最长子串
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
"""


class Solution1:
    """ BF """
    def lengthOfLongestSubstring(self, s: str) -> int:
        slen = len(s)
        if slen == 0:
            return 0

        res = 0
        for i in range(slen):
            hashtable = [-1] * 256
            j = 0
            while i + j < slen and hashtable[ord(s[i + j])] < 0:
                hashtable[ord(s[i + j])] = 1
                j += 1
            if res < j:
                res = j

        return res


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        i: head of the target str
        j: tail of the target str
        :param s:
        :return:
        """
        st = {}
        i, ans = 0, 0
        slen = len(s)
        for j in range(slen):
            if s[j] in st:
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans

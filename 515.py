"""
tag: 树；深度优先搜索；广度优先搜索
515. 在每个树行中找最大值
https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/
"""


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


import collections


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        res = list()
        if root is None:
            return res

        # deque.popleft() is faster than list.pop(0), because the deque
        # has been optimized to do popleft() approximately in O(1), while
        # list.pop(0) takes O(n).
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            level_res = list()
            for i in range(size):
                node = queue.popleft()
                level_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(max(level_res))
        return res

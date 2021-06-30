"""
tag: 树；广度优先搜索
107. 二叉树的层序遍历 II
https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
"""


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


import collections


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
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
            res.insert(0, level_res)
        return res
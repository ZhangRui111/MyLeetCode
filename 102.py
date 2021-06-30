"""
tag: 树；广度优先搜索
102. 二叉树的层序遍历
https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = list()
        if root is None:
            return res

        queue = list()
        queue.append(root)
        while queue:
            size = len(queue)
            level_res = list()
            for i in range(size):
                node = queue.pop(0)
                level_res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_res)
        return res

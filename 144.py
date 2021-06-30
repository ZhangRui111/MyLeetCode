"""
tag: 栈；树
144. 二叉树的前序遍历
https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """ Recursion """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder(root: TreeNode):  # 嵌套函数
            if root is None:
                return
            res.append(root.val)
            preorder(root.left)
            preorder(root.right)

        res = list()
        preorder(root)

        return res


class Solution2:
    """ Iteration """
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        if root is None:
            return res

        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right

        return res

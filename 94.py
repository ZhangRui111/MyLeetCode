"""
tag: 栈；树；哈希表
94. 二叉树的中序遍历
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """ Recursion """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder(root: TreeNode):  # 嵌套函数
            if root is None:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        res = list()
        inorder(root)

        return res


class Solution2:
    """ Iteration """
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        if root is None:
            return res

        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right

        return res

"""
tag: 栈；树
145. 二叉树的后序遍历
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """ Recursion """
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder(root: TreeNode):  # 嵌套函数
            if root is None:
                return

            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        res = list()
        postorder(root)

        return res


class Solution2:
    """ Iteration """
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = list()
        if root is None:
            return res

        stack = list()
        node = root
        prev = None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if node.right is None or node.right == prev:
                res.append(node.val)
                prev = node
                node = None
            else:
                stack.append(node)
                node = node.right

        return res

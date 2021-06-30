"""
tag: 树；深度优先搜索；广度优先搜索；递归；队列
199. 二叉树的右视图
https://leetcode-cn.com/problems/binary-tree-right-side-view/
"""


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


import collections


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
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
            res.append(level_res[-1])
        return res

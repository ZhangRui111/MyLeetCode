"""
tag: 树
637. 二叉树的层平均值
https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/
"""


# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


import collections


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
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
            res.append(sum(level_res)/len(level_res))
        return res

"""
tag: 树；深度优先搜索；广度优先搜索
117. 填充每个节点的下一个右侧节点指针 II
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/
"""


# # Definition for a Node.
# class Node:
#     def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.next = next


import collections


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        # deque.popleft() is faster than list.pop(0), because the deque
        # has been optimized to do popleft() approximately in O(1), while
        # list.pop(0) takes O(n).
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            prev = None
            for i in range(size):
                node = queue.popleft()
                if prev and prev != node:
                    prev.next = node
                prev = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

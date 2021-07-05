"""
tag:
232. 用栈实现队列
https://leetcode-cn.com/problems/implement-queue-using-stacks/
"""


from collections import deque


class MyQueue1:
    """ My solution """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackA = deque()
        self.stackB = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stackA:
            self.stackB.append(self.stackA.pop())
        self.stackB.append(x)
        while self.stackB:
            self.stackA.append(self.stackB.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stackA.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stackA[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stackA


class MyQueue2:
    """ 在 push() 优化掉不必要的一步 """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackA = deque()
        self.stackB = deque()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stackA:
            self.stackB.append(self.stackA.pop())
        self.stackA.append(x)  # 优化
        while self.stackB:
            self.stackA.append(self.stackB.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.stackA.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.stackA[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stackA

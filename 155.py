"""
tag: 栈，设计
155. 最小栈
https://leetcode-cn.com/problems/min-stack/
"""


class MinStack:
    """ My solution: 用辅助栈存储最小值的索引  """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_index = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_index:
            self.min_index.append(0)
        else:
            if val < self.stack[self.min_index[-1]]:
                self.min_index.append(len(self.stack) - 1)
            else:
                self.min_index.append(self.min_index[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_index.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.min_index[-1]]


class MinStack2:
    """ 用辅助栈存储最小值 """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_val = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_val:
            self.min_val.append(val)
        else:
            if val < self.min_val[-1]:
                self.min_val.append(val)
            else:
                self.min_val.append(self.min_val[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_val.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[-1]


# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-1)
# print(minStack.getMin())
# print(minStack.top())
# minStack.pop()
# print(minStack.getMin())

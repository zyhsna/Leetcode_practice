# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/23 10:23
# 文件名：implement-queue-using-stacks-lcci.py
# 开发工具：PyCharm
import collections
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.x = collections.deque([])
        # self.y = collections.deque([])


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.x.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.x.popleft()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.x[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if len(self.x) == 0:
            return False
        return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

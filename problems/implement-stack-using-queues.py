# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/12 16:57
# 文件名：implement-stack-using-queues.py
# 开发工具：PyCharm
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.List_store = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.List_store.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.List_store.pop()


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.List_store[len(self.List_store)]

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if len(self.List_store) == 0:
            return True
        return False

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/20 22:09
# 文件名：yong-liang-ge-zhan-shi-xian-dui-lie-lcof.py
# 开发工具：PyCharm
class CQueue(object):

    def __init__(self):
        self.stack_pop = []
        self.stack_push = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        while len(self.stack_pop) != 0:
            self.stack_push.append(self.stack_pop.pop())
        self.stack_push.append(value)
        while len(self.stack_push) != 0:
            self.stack_pop.append(self.stack_push.pop())

    def deleteHead(self):
        """
        :rtype: int
        """
        if len(self.stack_pop) == 0 and len(self.stack_push) == 0:
            return -1
        return self.stack_pop.pop()


tmp = CQueue()
# tmp.appendTail(1)
print(tmp.stack_pop)

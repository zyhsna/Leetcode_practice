# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/21 11:46
# 文件名：number-of-recent-calls.py
# 开发工具：PyCharm
import collections


class RecentCounter(object):
    def __init__(self):
        self.q = collections.deque()

    def ping(self, t):
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

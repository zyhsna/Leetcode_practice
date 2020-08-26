# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/26 10:50
# 文件名：delete-columns-to-make-sorted.py
# 开发工具：PyCharm
class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ans = 0
        for i in zip(*A):
            if list(i) != sorted(i):
                ans += 1

        return ans
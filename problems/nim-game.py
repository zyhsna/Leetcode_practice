# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/27 10:14
# 文件名：nim-game.py
# 开发工具：PyCharm
class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n %4 !=0
# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/28 9:26
# 文件名：number-of-1-bits.py
# 开发工具：PyCharm
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return str(bin(n)).count("1")
# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/11 9:29
# 文件名：check-permutation-lcci.py
# 开发工具：PyCharm
class Solution(object):
    def CheckPermutation(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        return set(s1) == set(s2)
# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/2 9:40
# 文件名：biao-shi-shu-zhi-de-zi-fu-chuan-lcof.py
# 开发工具：PyCharm
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except ValueError:
            return False

# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/5 10:42
# 文件名：add-digits.py
# 开发工具：PyCharm
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        while num >= 9:
            tmp = num
            tmp_sum = 0
            while tmp:
                tmp_sum += tmp % 10
                tmp /= 10
            num = tmp_sum
        return num
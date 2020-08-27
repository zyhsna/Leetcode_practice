# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/27 10:20
# 文件名：exchange-lcci.py
# 开发工具：PyCharm
class Solution(object):
    def exchangeBits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return ((num & 0x55555555) << 1) | ((num & 0xaaaaaaaa) >> 1);
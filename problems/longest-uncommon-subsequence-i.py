# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/29 9:57
# 文件名：longest-uncommon-subsequence-i.py
# 开发工具：PyCharm
class Solution(object):
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b :
            return -1
        return max(len(a),len(b))
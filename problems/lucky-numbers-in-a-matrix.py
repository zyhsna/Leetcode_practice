# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/24 11:01
# 文件名：lucky-numbers-in-a-matrix.py
# 开发工具：PyCharm
class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rowmin = [min(i) for i in matrix]
        colmin = [max(i) for i in zip(*matrix)]
        return [i for i in rowmin if i in colmin]
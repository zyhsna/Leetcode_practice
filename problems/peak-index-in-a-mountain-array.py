# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/24 10:59
# 文件名：peak-index-in-a-mountain-array.py
# 开发工具：PyCharm
class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))
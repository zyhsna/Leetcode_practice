# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/30 12:09
# 文件名：smallest-range-i.py
# 开发工具：PyCharm
class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(0, max(A) - min(A) - 2*K)
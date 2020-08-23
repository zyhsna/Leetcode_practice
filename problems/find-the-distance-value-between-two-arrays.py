# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/23 10:42
# 文件名：find-the-distance-value-between-two-arrays.py
# 开发工具：PyCharm
class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        return sum(all(abs(a1 - a2) > d for a2 in arr2) for a1 in arr1)

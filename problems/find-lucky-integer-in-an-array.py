# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/9 16:03
# 文件名：find-lucky-integer-in-an-array.py
# 开发工具：PyCharm
from collections import Counter

class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = Counter(arr)
        ans = 0
        for key, value in count.items():
            if key == value and key > ans:
                ans = key
        return ans

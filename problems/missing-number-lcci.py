# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/13 9:29
# 文件名：missing-number-lcci.py
# 开发工具：PyCharm
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = set(range(len(nums)+1)) - set(nums)
        return res.pop()
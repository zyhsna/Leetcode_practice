# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/24 11:34
# 文件名：intersection-of-two-arrays.py
# 开发工具：PyCharm
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return set(nums1) & set(nums2)
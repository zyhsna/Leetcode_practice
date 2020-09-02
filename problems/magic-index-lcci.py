# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/2 9:49
# 文件名：magic-index-lcci.py
# 开发工具：PyCharm
class Solution(object):
    def findMagicIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i == nums[i]:
                return i
        return -1
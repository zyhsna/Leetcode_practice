# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/17 12:18
# 文件名：majority-element.py
# 开发工具：PyCharm
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums) / 2]

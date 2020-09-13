# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/12 16:51
# 文件名：he-wei-sde-liang-ge-shu-zi-lcof.py
# 开发工具：PyCharm
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        # ans = 0
        while True:
            tmpsum = nums[start] + nums[end]
            if tmpsum == target:
                return [nums[start], nums[end]]
            if tmpsum > target:
                end -= 1
            if tmpsum < target:
                start += 1

# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/6 11:16
# 文件名：minimum-value-to-get-positive-step-by-step-sum.py
# 开发工具：PyCharm
class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        target = [0 for i in range(len(nums))]
        for i in range(len(nums)):
            if i == 0:
                target[0] = nums[0]
            else:
                target[i] = target[i - 1] + nums[0]
        return min(target) + 1 if min(target) <= 0 else 1



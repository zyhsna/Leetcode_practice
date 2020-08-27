# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/27 10:27
# 文件名：minimum-subsequence-in-non-increasing-orde.py
# 开发工具：PyCharm
class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        tmp = sum(nums) / 2
        for i in range(len(nums) - 1, -1, -1):
            if sum(nums[i:]) > tmp: break

        return nums[i:][::-1]

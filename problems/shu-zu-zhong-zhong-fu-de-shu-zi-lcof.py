# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/6 11:25
# 文件名：shu-zu-zhong-zhong-fu-de-shu-zi-lcof.py
# 开发工具：PyCharm
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        # occurrence = {}
        # for i in nums:
        #     if i in occurrence.keys():
        #         return i
        #     else:
        #         occurrence[i] = 1

        nums.sort()
        start = 1
        while start < len(nums):
            if nums[start] == nums[start-1]:
                return nums[start]
            start += 1
        return

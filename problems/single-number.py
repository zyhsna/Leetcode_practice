# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/26 10:52
# 文件名：single-number.py
# 开发工具：PyCharm
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = {}
        for i in nums:
            if i not in ans.keys():
                ans[i] = 1
            else:
                ans[i] += 1
        for key, value in ans.items():
            if value == 1:
                return key


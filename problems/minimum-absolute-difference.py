# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/9 10:59
# 文件名：minimum-absolute-difference.py
# 开发工具：PyCharm
class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: list[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        ans = []
        difference = 1000000
        for i in range(1, len(arr)):
            num =  abs(arr[i] - arr[i - 1])
            if num < difference:
                difference = num
                ans = []
                ans.append([arr[i], arr[i - 1]])
            elif num == difference:
                ans.append([arr[i], arr[i - 1]])
        return ans


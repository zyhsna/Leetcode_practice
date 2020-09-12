# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/12 9:23
# 文件名：count-largest-group.py
# 开发工具：PyCharm
class Solution(object):
    def countLargestGroup(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = {}
        for i in range(1, n):
            tmpsum = 0
            while i != 0:
                tmpsum += i % 10
                i /= 10
            if tmpsum in count.keys():
                count[tmpsum] += 1
            else:
                count[tmpsum] = 1
        ans = 0
        Max = 0
        for key, value in count.items():
            if value > Max:
                Max = value
                ans = 1
            if value == Max:
                ans += 1
        return ans

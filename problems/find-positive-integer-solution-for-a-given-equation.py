# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/28 9:25
# 文件名：find-positive-integer-solution-for-a-given-equation.py
# 开发工具：PyCharm
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
"""

class Solution(object):
    def findSolution(self, customfunction, z):
        """
        :type num: int
        :type z: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(1,z+1):
            for j in range(1,z+1):
                if customfunction.f(i,j)==z:
                    tmp = [i,j]
                    ans.append(tmp)

        return ans
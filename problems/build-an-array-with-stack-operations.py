# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/15 12:33
# 文件名：build-an-array-with-stack-operations.py
# 开发工具：PyCharm
class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        res = []
        for num in range(1, target[-1]+1):
            res.append('Push')
            if num not in target:
                res.append('Pop')
        return res

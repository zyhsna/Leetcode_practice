# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/8 11:05
# 文件名：combinations.py
# 开发工具：PyCharm
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        def dfs(n, k, ret, j):
            if len(ret) == k:
                res.append(ret)
                return

            for i in range(j + 1, n + 1):
                dfs(n, k, ret + [i], i)

        res = []
        dfs(n, k, [], 0)
        return res
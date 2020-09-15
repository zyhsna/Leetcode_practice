# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/15 12:16
# 文件名：matrix-cells-in-distance-order.py
# 开发工具：PyCharm
class Solution(object):
    def allCellsDistOrder(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(R):
            for j in range(C):
                res.append([abs(r0 - i) + abs(c0 - j), [i, j]])
        res = sorted(res, key=lambda x: x[0])
        ans = []
        for i in res:
            ans.append(i[1])
        return ans

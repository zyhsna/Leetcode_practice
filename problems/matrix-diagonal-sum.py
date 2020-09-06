# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/6 10:39
# 文件名：matrix-diagonal-sum.py
# 开发工具：PyCharm
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ans = 0
        length = len(mat[0])
        j = 0
        for i in range(len(mat)):
            j1 = length - j - 1
            if j1 == j:
               ans += mat[i][j]
            else:
                ans = mat[i][j] + mat[i][j1] + ans
            j+=1
        return ans
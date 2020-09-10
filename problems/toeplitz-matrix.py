# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/10 16:55
# 文件名：toeplitz-matrix.py
# 开发工具：PyCharm
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: list[list[int]]
        :rtype: bool
        """
        times = len(matrix)+len(matrix[0])
        for i in range(1, len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i-1][j-1] != matrix[i][j]:
                    return False
        return True



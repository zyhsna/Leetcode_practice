# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/22 11:20
# 文件名：squares-of-a-sorted-array.py
# 开发工具：PyCharm
import numpy as np


def sortedSquares(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    A = np.array(A)
    A = A * A
    A.sort()
    return A.tolist()


print(sortedSquares(1, [-4, -1, 0, 3, 10]))

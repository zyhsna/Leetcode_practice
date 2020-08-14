# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/14 16:27
# 文件名：count-negative-numbers-in-a-sorted-matrix.py
# 开发工具：PyCharm
import numpy as np


def countNegatives(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    grid = np.array(grid)
    return len(np.extract(grid<0, grid))


print(countNegatives(1,[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))

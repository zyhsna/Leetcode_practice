# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/15 10:34
# 文件名：cells-with-odd-values-in-a-matrix.py
# 开发工具：PyCharm
import numpy as np


def oddCells(self, n, m, indices):
    """
    :type n: int
    :type m: int
    :type indices: List[List[int]]
    :rtype: int
    """
    arr = np.zeros((n, m))
    indices = np.array(indices)
    row = len(indices)
    col = len(indices[0])
    for i in range(row):
        for j in range(col):
            if j is 0:  # 指定的第j行
                arr[indices[i, j], :] += 1
            else:  # 指定的第j列
                arr[:, indices[i, j]] += 1
    return len(np.extract(arr % 2 != 0, arr))


print(oddCells(1, 48, 37, [[40, 5]]))

# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/15 14:44
# 文件名：flipping-an-image.py
# 开发工具：PyCharm
def flipAndInvertImage(self, A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    # 一行代码
    # return    [[j ^ 1 for j in i[::-1]] for i in A]
    # 一般做法的优化

    for i in range(len(A)):
        for j in range((len(A) + 1) // 2):
            if A[i][j] == A[i][-1 - j]:  # 如果不等的话，第一遍翻转再取反就相当于一开始不变
                t = 1 - A[i][j]
                A[i][j] = A[i][-1 - j] = t
    return A

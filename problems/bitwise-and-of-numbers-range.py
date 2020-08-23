# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/23 8:06
# 文件名：bitwise-and-of-numbers-range.py
# 开发工具：PyCharm
def rangeBitwiseAnd(self, m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    i = 0
    while m != n:
        m >>= 1
        n >>= 1
        i += 1
    return m << i

# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/8 17:22
# 文件名：hamming-distance.py
# 开发工具：PyCharm
def hammingDistance(self, x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return bin(x ^ y).count('1')
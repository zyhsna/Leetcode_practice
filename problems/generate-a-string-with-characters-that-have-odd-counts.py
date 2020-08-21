# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/20 22:03
# 文件名：generate-a-string-with-characters-that-have-odd-counts.py
# 开发工具：PyCharm
def generateTheString(self, n):
    """
    :type n: int
    :rtype: str
    """
    return "a" * n if n % 2 != 0 else "a" * (n - 1) + "b"
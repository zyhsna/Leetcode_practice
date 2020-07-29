# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/27 17:54
# 文件名：xor-operation-in-an-array.py
# 开发工具：PyCharm
def xorOperation(n, start):
    """
    :type n: int
    :type start: int
    :rtype: int
    """
    ans = 0
    num = [start + x * 2 for x in range(n)]
    for i in num:
        ans = ans ^ i
    return ans

print(xorOperation(1, 7))
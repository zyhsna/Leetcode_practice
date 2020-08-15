# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/15 14:32
# 文件名：maximum-69-number.py
# 开发工具：PyCharm
def maximum69Number(self, num):
    """
    :type num: int
    :rtype: int
    """
    return str(num).replace("6", "9", 1)


print(maximum69Number(1, 9966))

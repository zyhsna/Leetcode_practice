# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/28 17:31
# 文件名：number-of-steps-to-reduce-a-number-to-zero.py
# 开发工具：PyCharm
def numberOfSteps(self, num):
    """
    :type num: int
    :rtype: int
    """
    count = 0
    while num !=0:
        if num % 2 == 0:
            num/=2
        else:
            num -= 1
        count += 1
    return count
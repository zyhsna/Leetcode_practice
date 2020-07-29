# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/28 17:21
# 文件名：subtract-the-product-and-sum-of-digits-of-an-integer.py
# 开发工具：PyCharm
def subtractProductAndSum(self, n):
    """
    :type n: int
    :rtype: int
    """
    sum = 0
    multi = 1
    while n > 0:
        temp = n%10
        sum += temp
        multi *= temp
        n //= 10
    print(multi - sum)

subtractProductAndSum(1, 4421)
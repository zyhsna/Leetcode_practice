# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/17 17:52
# 文件名：find-n-unique-integers-sum-up-to-zero.py
# 开发工具：PyCharm
def sumZero(self, n):
    """
    :type n: int
    :rtype: List[int]
    """
    return range(1 - n, n, 2)
    # 看评论区dalao写出来的，不然我还在想用循环写

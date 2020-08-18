# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/18 17:17
# 文件名：self-dividing-numbers.py
# 开发工具：PyCharm
def selfDividingNumbers(self, left: int, right: int):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """

    # for i in range(left, right+1):
    #
    return [n for n in range(left, right + 1) if "0" not in str(n) and all([n % int(b) == 0 for b in str(n)])]

print(selfDividingNumbers(1,1,22))
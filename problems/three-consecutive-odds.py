# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/19 11:08
# 文件名：three-consecutive-odds.py
# 开发工具：PyCharm
def threeConsecutiveOdds(self, arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    for i in range(2, len(arr)):
        if arr[i - 2] % 2 != 0 and arr[i - 1] % 2 != 0 and arr[i] % 2 != 0:
            return True

    return False


print(threeConsecutiveOdds(1,[1,2,34,3,4,5,7,23,12]))

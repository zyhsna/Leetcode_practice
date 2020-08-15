# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/15 11:12
# 文件名：can-make-arithmetic-progression-from-sequence.py
# 开发工具：PyCharm
def canMakeArithmeticProgression(self, arr):
    """
    :type arr: List[int]
    :rtype: bool
    """
    arr = sorted(arr)
    diff = arr[1] - arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i + 1] - arr[i] != diff:
            return False
    return True


# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/30 18:44
# 文件名：how-many-numbers-are-smaller-than-the-current-number.py
# 开发工具：PyCharm
def smallerNumbersThanCurrent(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = [0] * 101
    for i in nums:
        ans[i] += 1
    return [sum(ans[:n]) for n in nums]

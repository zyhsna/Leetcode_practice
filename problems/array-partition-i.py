# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/21 11:28
# 文件名：array-partition-i.py
# 开发工具：PyCharm
def arrayPairSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums = sorted(nums)
    return sum(nums[::2])


print(arrayPairSum(1, [1,4,3,2]))
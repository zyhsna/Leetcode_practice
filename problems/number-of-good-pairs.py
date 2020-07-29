# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/26 17:56
# 文件名：number-of-good-pairs.py
# 开发工具：PyCharm

def numIdenticalPairs(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(nums):
        for j in range(i+1, len(nums)):
            if nums[j] == nums[i] and j>i:
                count += 1
    return count

numIdenticalPairs([1,2,3,1,1,3])
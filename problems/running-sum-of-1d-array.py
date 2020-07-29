# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/26 17:47
# 文件名：running-sum-of-1d-array.py
# 开发工具：PyCharm

# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#
# Return the running sum of nums.

def runningSum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = [0 for x in range(len(nums))]

    ans[0] = nums[0]
    for i in range(1,len(nums)):
        ans[i] = ans[i-1]+nums[i]
    return ans


print(runningSum([1,1,1,1]))
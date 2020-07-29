# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/26 17:35
# 文件名：Two sum.py
# 开发工具：PyCharm
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    ans = []
    flag = False
    for i in range(len(nums)):
        if flag:
            break
        else:
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    flag = True
                    break

    return ans

nums= [2, 7, 11, 15]
print(twoSum(nums, 26))
# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/30 18:31
# 文件名：create-target-array-in-the-given-order.py
# 开发工具：PyCharm
def createTargetArray(self, nums, index):
    """
    :type nums: List[int]
    :type index: List[int]
    :rtype: List[int]
    """
    ans = []
    for i in range(len(nums)):
        ans.insert(index[i], nums[i])

    return ans

print(createTargetArray(1,[0,1,2,3,4], [0,1,2,2,1]))

# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/3 20:59
# 文件名：maximum-product-of-two-elements-in-an-array.py
# 开发工具：PyCharm

def maxProduct(self, nums) -> int:
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) is 2:
        return (nums[0] - 1) * (nums[1] - 1)
    else:
        maxNum = nums[0] if nums[0] > nums[1] else nums[1]
        secNum = nums[1] if nums[0] > nums[1] else nums[0]
        for i in range(2, len(nums)):
            if nums[i] >= maxNum:
                secNum = maxNum
                maxNum = nums[i]
            elif secNum <= nums[i] < maxNum:
                secNum = nums[i]
        return (maxNum - 1) * (secNum - 1)

print(maxProduct(1, [3,7]))

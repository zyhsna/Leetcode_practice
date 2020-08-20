# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/19 10:59
# 文件名：convert-sorted-array-to-binary-search-tree.py
# 开发工具：PyCharm
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def sortedArrayToBST(self, nums):
    """
    :type nums: List[int]
    :rtype: TreeNode
    """
    if not nums: return None
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    leftNums, rightNums = nums[:mid], nums[mid + 1:]
    root.left = self.sortedArrayToBST(leftNums)
    root.right = self.sortedArrayToBST(rightNums)
    return root

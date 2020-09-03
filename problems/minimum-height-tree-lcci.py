# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/3 10:03
# 文件名：minimum-height-tree-lcci.py
# 开发工具：PyCharm
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        n = len(nums) // 2
        root = TreeNode(nums[n])
        left = nums[0: n]
        right = nums[n + 1:]
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)
        return root

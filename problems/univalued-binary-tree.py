# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/5 9:39
# 文件名：univalued-binary-tree.py
# 开发工具：PyCharm
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root or (not root.left and not root.right):
            return True
        val = root.val

        def helper(root, val):

            if root.left and root.right:
                return helper(root.left, val) and helper(root.right, val) and root.val == val
            if root.left and not root.right:
                return helper(root.left, val) and root.val == val
            if root.right and not root.left:
                return helper(root.right, val) and root.val == val
            if root.val != val:
                return False
            else:
                return True

        if root.left and root.right:
            return helper(root.left, val) and helper(root.right, val) and root.val == val
        elif root.left and not root.right:
            return helper(root.left, val) and root.val == val
        elif root.right and not root.left:
            return helper(root.right, val) and root.val == val

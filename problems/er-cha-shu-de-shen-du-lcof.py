# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/6 17:30
# 文件名：er-cha-shu-de-shen-du-lcof.py
# 开发工具：PyCharm
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def maxDepth(self, root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root: return 0
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

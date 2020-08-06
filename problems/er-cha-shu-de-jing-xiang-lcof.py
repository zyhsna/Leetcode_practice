# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/6 17:59
# 文件名：er-cha-shu-de-jing-xiang-lcof.py
# 开发工具：PyCharm
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def mirrorTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root: return
    root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
    return root

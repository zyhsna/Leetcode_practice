# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/28 9:53
# 文件名：er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof.py
# 开发工具：PyCharm
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root

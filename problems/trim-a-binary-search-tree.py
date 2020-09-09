# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/9 10:52
# 文件名：trim-a-binary-search-tree.py
# 开发工具：PyCharm
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return root

        if (root.val < L):
            return self.trimBST(root.right, L, R)
        if (root.val > R):
            return self.trimBST(root.left, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        return root

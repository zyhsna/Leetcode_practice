# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/10 17:06
# 文件名：sum-of-root-to-leaf-binary-numbers.py
# 开发工具：PyCharm
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = []

        def helper(root, tmp_val):
            tmp_val += str(root.val)
            if not root.left and not root.right:
                ans.append(tmp_val)
                return

            if root.left:
                helper(root.left, tmp_val)
            if root.right:
                helper(root.right, tmp_val)

        helper(root, "0")
        Sum = 0

        for i in ans:
            Sum += int(i, 2)
        return Sum
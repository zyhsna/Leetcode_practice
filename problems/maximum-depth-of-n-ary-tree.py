# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/24 11:50
# 文件名：maximum-depth-of-n-ary-tree.py
# 开发工具：PyCharm
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        if not root.children:
            return 1
        return max(self.maxDepth(child)+1 for child in root.children)
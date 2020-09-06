# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/6 10:18
# 文件名：binary-tree-level-order-traversal-ii.py
# 开发工具：PyCharm
# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        levelList = deque([])
        levelList.append(root)
        while len(levelList) != 0:
            tmp = []
            for _ in range(len(levelList)):
                root = levelList.popleft()
                tmp.append(root.val)
                if root.left:
                    levelList.append(root.left)
                if root.right:
                    levelList.append(root.right)
            ans.append(tmp)

        return ans.reverse()

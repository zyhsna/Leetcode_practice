# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/12 9:04
# 文件名：average-of-levels-in-binary-tree.py
# 开发工具：PyCharm
# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans = []
        if not root:
            return []
        levelnode = deque([])
        levelnode.append(root)
        while levelnode:
            length = len(levelnode)
            levelsum = 0
            for _ in range(length):
                root = levelnode.popleft()
                levelsum += root.val
                if root.left: levelnode.append(root.left)
                if root.right: levelnode.append(root.right)
            ans.append(int(str(levelsum / length).split(".")[0]))
        return ans





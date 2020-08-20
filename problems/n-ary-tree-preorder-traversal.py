# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/20 11:09
# 文件名：n-ary-tree-preorder-traversal.py
# 开发工具：PyCharm
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        # ans = []
        # if root is None:
        #     return ans
        # ans.append(root.val)
        # for child in root.children:
        #     self.preorder(child)
        # return root
        ans = []

        def helper(root):
            if not root:
                return
            ans.append(root.val)
            for child in root.children:
                helper(child)

        helper(root)
        return ans

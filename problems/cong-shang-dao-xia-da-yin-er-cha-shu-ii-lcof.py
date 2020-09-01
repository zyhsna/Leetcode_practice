# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/1 10:19
# 文件名：cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof.py
# 开发工具：PyCharm
# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        array = deque([])
        ans = []
        array.append(root)
        while array:
            tmp = []
            for _ in range(len(array)):
                tmp_node = array.popleft()
                tmp.append(tmp_node.val)
                if tmp_node.left:
                    array.append(tmp_node.left)
                if tmp_node.right:
                    array.append(tmp_node.right)
            ans.append(tmp)
        return ans



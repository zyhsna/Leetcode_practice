# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/9 11:00
# 文件名：range-sum-of-bst.py
# 开发工具：PyCharm
def rangeSumBST(self, root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: int
    """

    def dfs(node):
        if node:
            if L <= node.val <= R:
                self.ans += node.val
            if L < node.val:
                dfs(node.left)
            if node.val < R:
                dfs(node.right)

    self.ans = 0
    dfs(root)
    return self.ans
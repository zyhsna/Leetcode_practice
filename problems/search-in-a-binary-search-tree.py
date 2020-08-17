# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/17 18:29
# 文件名：search-in-a-binary-search-tree.py
# 开发工具：PyCharm
def searchBST(self, root, val):
    """
    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    if root is None or val == root.val:
        return root

    return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)
# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/14 16:17
# 文件名：invert-binary-tree.py
# 开发工具：PyCharm
def invertTree(self, root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return
    root.left, root.right = root.right, root.left
    invertTree(root.left)
    invertTree(root.right)
    return root
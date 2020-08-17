# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/17 17:25
# 文件名：balanced-binary-tree.py
# 开发工具：PyCharm
def isBalanced(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def height(root):
        if not root:
            return 0
        return max(height(root.left), height(root.right)) + 1

    if not root:
        return True
    return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(
        root.right)
# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/9 11:12
# 文件名：merge-two-binary-trees.py
# 开发工具：PyCharm
def mergeTrees(self, t1, t2):
    """
    :type t1: TreeNode
    :type t2: TreeNode
    :rtype: TreeNode
    """
    if not (t1 and t2):
        return t1 if t1 else t2
    t1.val += t2.val
    t1.left = self.mergeTrees(t1.left, t2.left)
    t1.right = self.mergeTrees(t1.right, t2.right)
    return t1
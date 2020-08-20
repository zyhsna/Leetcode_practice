# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/18 17:08
# 文件名：n-ary-tree-postorder-traversal.py
# 开发工具：PyCharm
def postorder(self, root):
    """
    :type root: Node
    :rtype: List[int]
    """
    ans = []

    def helper(root):
        if root:
            for child in root.children:
                helper(child)
            ans.append(root.val)

    helper(root)
    return ans
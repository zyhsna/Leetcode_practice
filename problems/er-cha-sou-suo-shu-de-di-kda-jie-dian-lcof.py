# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/18 16:57
# 文件名：er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof.py
# 开发工具：PyCharm
def kthLargest(self, root, k: int) -> int:
    def helper(root):
        return helper(root.left) + [root.val] + helper(root.right) if root else []

    return helper(root)[-k]
# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/3 21:23
# 文件名：submissions.py
# 开发工具：PyCharm
def destCity(self, paths):
    """
    :type paths: List[List[str]]
    :rtype: str
    """
    P0 = [path[0] for path in paths]  # 将出发地放进一个数组里。
    for path in paths:
        # 如果目的地不在出发地列表里，则该目的地是最终目的地。
        if path[1] not in P0:
            return path[1]
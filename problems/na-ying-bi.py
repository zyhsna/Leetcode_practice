# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/29 18:52
# 文件名：na-ying-bi.py
# 开发工具：PyCharm
def minCount(self, coins):
    """
    :type coins: List[int]
    :rtype: int
    """
    count = 0
    for i in coins:
        while i != 0:
            if i >= 2:
                i -= 2
            else:
                i -= 1
            count += 1
    return count


print(minCount(1, [4, 2, 1]))

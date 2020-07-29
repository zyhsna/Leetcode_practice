# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/28 10:57
# 文件名：jewels-and-stones.py
# 开发工具：PyCharm
def numJewelsInStones(J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    count = 0
    for i in J:
        count += S.count(i)
    return count

numJewelsInStones("z", "AZZZ")
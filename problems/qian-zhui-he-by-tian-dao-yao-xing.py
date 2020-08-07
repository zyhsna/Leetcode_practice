# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/7 17:47
# 文件名：qian-zhui-he-by-tian-dao-yao-xing.py
# 开发工具：PyCharm
def balancedStringSplit(self, s):
    """
    :type s: str
    :rtype: int
    """
    if not s: return 0
    count = 0
    res = 0
    m = len(s)
    i = 0
    while i < m:
        if count == 0:
            res += 1
        if s[i] == 'R':
            count += 1
        else:
            count -= 1
        i += 1
    return res

# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/17 21:06
# 文件名：is-unique-lcci.py
# 开发工具：PyCharm
def isUnique(self, astr):
    """
    :type astr: str
    :rtype: bool
    """
    return len(set(astr)) == len(astr)
    # 刚好今天看到the fluent python 中有set这个方法

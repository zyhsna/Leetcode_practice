# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/25 9:46
# 文件名：groups-of-special-equivalent-strings.py
# 开发工具：PyCharm
class Solution(object):
    def numSpecialEquivGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        res = set()
        for sub in A:
            sub = ''.join(sorted(sub[::2]) + sorted(sub[1::2]))
            res.add(sub)
        return len(res)
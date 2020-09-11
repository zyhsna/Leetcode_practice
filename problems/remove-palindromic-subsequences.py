# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/11 10:06
# 文件名：remove-palindromic-subsequences.py
# 开发工具：PyCharm
class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if not s else 1 if s[::-1] == s else 2
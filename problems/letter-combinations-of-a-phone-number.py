# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/26 9:57
# 文件名：letter-combinations-of-a-phone-number.py
# 开发工具：PyCharm
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        ans = [""]
        for num in digits:
            ans = [pre+suf for pre in ans for suf in KEY[num]]
        return ans
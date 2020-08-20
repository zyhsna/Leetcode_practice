# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/19 9:24
# 文件名：palindromic-substrings.py
# 开发工具：PyCharm
def countSubstrings(self, s):
    """
    :type s: str
    :rtype: int
    """
    num = 0

    def count(start: int, end: int, num: int):
        while start >= 0 and end < len(s) and s[start] == s[end]:
            num += 1
            start -= 1
            end += 1
        return num

    for i in range(len(s)):
        num = count(i, i, num)
        num = count(i, i + 1, num)

    return num


print(countSubstrings(1, "aba"))

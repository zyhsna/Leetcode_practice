# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/22 11:03
# 文件名：reverse-words-in-a-string-iii.py
# 开发工具：PyCharm
def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    s = s[::-1]
    s = s.split(' ')
    s.reverse()
    return ' '.join(s)


print(reverseWords(1, "Let's take LeetCode contest"))

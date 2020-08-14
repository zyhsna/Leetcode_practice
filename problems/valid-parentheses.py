# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/14 16:04
# 文件名：valid-parentheses.py
# 开发工具：PyCharm
def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """

    if len(s) % 2 == 1:
        return False

    pairs = {
        ")": "(",
        "]": "[",
        "}": "{",
    }
    stack = list()
    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
        else:
            stack.append(ch)

    return not stack
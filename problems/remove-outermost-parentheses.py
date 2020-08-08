# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/8 16:41
# 文件名：remove-outermost-parentheses.py
# 开发工具：PyCharm
def removeOuterParentheses(self, S):
    """
    :type S: str
    :rtype: str
    """
    count = 0
    distance = 0
    x = [0 for i in range(len(S))]
    for i in range(len(S)):
        if S[i] is "(":
            count += 1
            distance += 1
        elif S[i] is ")" and count is 1:
            x[i - distance] = x[i] = 1
            distance = 0
            count -= 1
        elif S[i] is ")":
            distance += 1
            count -= 1
    ans = ""
    for i in range(len(S)):
        if x[i] is  0:
            ans += S[i]
    return ans


print(removeOuterParentheses(1, "(()())(())"))

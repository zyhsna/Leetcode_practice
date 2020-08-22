# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/21 11:06
# 文件名：di-string-match.py
# 开发工具：PyCharm
def diStringMatch(self, S):
    """
    :type S: str
    :rtype: List[int]
    """
    left, right = 0, len(S)
    ans = []
    for i in S:
        if i is "I":
            ans.append(left)
            left += 1
        else:
            ans.append(right)
            right -= 1
    ans.append(left)
    return ans

print(diStringMatch(1, "IDID"))

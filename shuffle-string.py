# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/30 18:54
# 文件名：shuffle-string.py
# 开发工具：PyCharm

def getSecond(elem):
    return elem[0]


def restoreString(self, s: str, indices: list[int]) -> str:
    """
    :type s: str
    :type indices: List[int]
    :rtype: str
    """
    ans = ""
    temp = [[0, 0] for x in range(len(indices))]
    for i in range(len(indices)):
        temp[i][0] = indices[i]
        temp[i][1] = s[i]
    temp.sort(key=getSecond)
    for i in range(len(temp)):
        ans += temp[i][1]
    return ans


print(restoreString(1, "codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))

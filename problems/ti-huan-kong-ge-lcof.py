# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/9 11:01
# 文件名：ti-huan-kong-ge-lcof.py
# 开发工具：PyCharm
def replaceSpace(self, s) -> str:
    """
    :type s: str
    :rtype: str
    """
    # location = [0 for x in range(len(s))]
    # for i in range(len(s)):
    #     if s[i] is " ":
    #         location[i] = 1
    # ans = ""
    # for i in range(len(location)):
    #     if location[i] is 0:
    #         ans += s[i]
    #     else:
    #         ans += "%20"
    # return ans
    """another answer"""
    return s.replace(" ", "%20")


# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/17 18:16
# 文件名：decrypt-string-from-alphabet-to-integer-mapping.py
# 开发工具：PyCharm
def freqAlphabets(self, s:str):
    """
    :type s: str
    :rtype: str
    """
    def get(string):
        return chr(int(string) + 96)

    i, ans = 0, ""
    while i < len(s):
        if i + 2 < len(s) and s[i + 2] == '#':
            ans += get(s[i: i + 2])
            i += 2
        else:
            ans += get(s[i])
        i += 1
    return ans



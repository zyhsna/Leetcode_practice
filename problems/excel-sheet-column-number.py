# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/4 9:48
# 文件名：excel-sheet-column-number.py
# 开发工具：PyCharm
class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            position = len(s)-i-1
            ans += (26**position)*(ord(s[i])-ord("A")+1)

        return ans

test = Solution()
print(test.titleToNumber("ZY"))
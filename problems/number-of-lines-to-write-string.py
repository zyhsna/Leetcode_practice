# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/12 16:45
# 文件名：number-of-lines-to-write-string.py
# 开发工具：PyCharm
class Solution:
    def numberOfLines(self, widths: list[int], S: str) -> list[int]:
        count = 0
        lines = 0
        for s in S:
            count += widths[ord(s) - 97]
            if count == 100:
                lines += 1
                count = 0
            elif count > 100:
                lines += 1
                count = widths[ord(s) - 97]

        return [lines + 1, count]

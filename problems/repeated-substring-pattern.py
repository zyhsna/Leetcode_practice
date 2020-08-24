# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/24 10:29
# 文件名：repeated-substring-pattern.py
# 开发工具：PyCharm
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # example = set((reversed(s)))
        # example = "".join(example)
        # example = example[::-1]
        # if len(s) % len(example) != 0:
        #     return False
        # for i in range(len(s)-len(example), len(example)):
        #     if s[i:i+len(example)] != example:
        #         return False
        # return True
        return s in (s + s)[1:-1]
test = Solution()
print(test.repeatedSubstringPattern(1, "ababba"))

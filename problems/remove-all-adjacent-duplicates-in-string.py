# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/1 11:51
# 文件名：remove-all-adjacent-duplicates-in-string.py
# 开发工具：PyCharm
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        # 初始化栈
        stack = []
        # 遍历栈元素
        for e in S:
            if stack and stack[-1] == e:
                stack.pop()
            else:
                stack.append(e)
        return "".join(stack)
test = Solution()
print(test.removeDuplicates("abbaca"))

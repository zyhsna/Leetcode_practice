# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/4 9:33
# 文件名：baseball-game.py
# 开发工具：PyCharm
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for i in ops:
            if i is "C":
                stack.pop()
                continue
            if i is "D":
                stack.append(stack[len(stack)-1]*2)
                continue
            if i is "+":
                stack.append(stack[len(stack)-1]+stack[len(stack)-2])
                continue
            stack.append(int(i))
        return sum(stack)

test = Solution()
print(test.calPoints(["5","2","C","D","+"]))


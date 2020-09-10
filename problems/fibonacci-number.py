# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/10 11:14
# 文件名：fibonacci-number.py
# 开发工具：PyCharm
class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==0 or N==1:
            return N

        return self.fib(N-1)+self.fib(N-2)

test = Solution()
print(test.fib(5))
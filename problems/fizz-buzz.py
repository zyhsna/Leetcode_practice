# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/15 12:36
# 文件名：fizz-buzz.py
# 开发工具：PyCharm
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = [str(i) for i in range(1, n + 1)]
        for i in range(len(ans)):
            tmp = int(ans[i])
            if tmp % 3 == 0 and tmp % 5 != 0:
                ans[i] = "Fizz"
                continue
            if tmp % 3 != 0 and tmp % 5 == 0:
                ans[i] = "Buzz"
                continue
            if tmp % 15 == 0:
                ans[i] = "FizzBuzz"
                continue
        return ans
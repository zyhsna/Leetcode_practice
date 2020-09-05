# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/5 10:25
# 文件名：average-salary-excluding-the-minimum-and-maximum-salary.py
# 开发工具：PyCharm
class Solution(object):
    def average(self, salary):
        """
        :type salary: list[int]
        :rtype: float
        """
        salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary) / len(salary)

test = Solution()
print(test.average([4000,3000,1000,2000]))
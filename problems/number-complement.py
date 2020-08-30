# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/30 11:54
# 文件名：number-complement.py
# 开发工具：PyCharm
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(str(bin(num))[2:].replace("0", "2").replace("1", "0").replace("2", "1"), 2)


test = Solution()
print(test.findComplement(5))

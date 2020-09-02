# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/2 9:55
# 文件名：prime-number-of-set-bits-in-binary-representation.py
# 开发工具：PyCharm
class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """

        count = 0
        temp = [2, 3, 5, 7, 11, 13, 17, 19]
        for i in range(L, R + 1):
            one_count = str(bin(i)).count("1")
            if one_count in temp:
                count += 1
        return  count


test = Solution()
print(test.countPrimeSetBits(842, 888))

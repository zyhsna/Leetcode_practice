# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/29 10:01
# 文件名：water-bottles.py
# 开发工具：PyCharm
class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        empty_bottle = numBottles
        while empty_bottle >= numExchange:
            new_bottle = empty_bottle // numExchange
            numBottles += new_bottle

            empty_bottle -= numExchange*new_bottle - new_bottle

        return numBottles

test = Solution()
print(test.numWaterBottles(9, 3))
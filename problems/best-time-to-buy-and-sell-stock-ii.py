# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/18 9:19
# 文件名：best-time-to-buy-and-sell-stock-ii.py
# 开发工具：PyCharm
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: list[int]
        :rtype: int
        """
        profile = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                profile += prices[i+1] - prices[i]
        return profile
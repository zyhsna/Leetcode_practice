# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/20 11:27
# 文件名：final-prices-with-a-special-discount-in-a-shop.py
# 开发工具：PyCharm
def finalPrices(self, prices):
    """
    :type prices: List[int]
    :rtype: List[int]
    """

    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[i] >= prices[j]:
                prices[i] -= prices[j]
                break
    return prices

print(finalPrices(1, [1,2,3,4]))

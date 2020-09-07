# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/6 17:41
# 文件名：distribute-candies.py
# 开发工具：PyCharm
class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(set(candies)), len(candies) // 2)
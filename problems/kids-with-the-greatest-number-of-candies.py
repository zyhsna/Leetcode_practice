# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/27 17:24
# 文件名：kids-with-the-greatest-number-of-candies.py
# 开发工具：PyCharm
def kidsWithCandies(candies, extraCandies):
    """
    :type candies: List[int]
    :type extraCandies: int
    :rtype: List[bool]
    """
    max_num = max(candies)
    for i in range(len(candies)):
        if candies[i]+extraCandies >= max_num:
            candies[i] = True
        else:
            candies[i] = False
    return candies



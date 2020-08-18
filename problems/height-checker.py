# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/18 17:34
# 文件名：height-checker.py
# 开发工具：PyCharm
def heightChecker(self, heights: list):
    """
    :type heights: List[int]
    :rtype: int
    """
    # sorted_height = sorted(heights)
    # count = 0
    # for i in range(len(heights)):
    #     if sorted_height[i] != heights[i]:
    #         count += 1
    # return count

    # only one line code
    return len([n for n in range(len(heights)) if heights[n] != sorted(heights)[n]])


print(heightChecker(1, [1, 1, 4, 2, 1, 3]))

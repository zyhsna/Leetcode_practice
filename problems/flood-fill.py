# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/16 8:40
# 文件名：flood-fill.py
# 开发工具：PyCharm
def floodFill(self, image, sr, sc, newColor):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type newColor: int
    :rtype: List[List[int]]
    """
    a = image[sr][sc]
    if a == newColor:
        return image
    longth, width = len(image), len(image[0])

    def goon(i, j):
        if 0 <= i < longth and 0 <= j < width and image[i][j] == a:
            image[i][j] = newColor
            goon(i - 1, j)
            goon(i + 1, j)
            goon(i, j - 1)
            goon(i, j + 1)

    goon(sr, sc)
    return image
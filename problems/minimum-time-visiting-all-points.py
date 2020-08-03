# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/3 17:43
# 文件名：minimum-time-visiting-all-points.py
# 开发工具：PyCharm
def minTimeToVisitAllPoints(self, points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    time = 0
    for i in range(len(points) - 1):
        distance_x = abs(points[i][0] - points[i + 1][0])
        distance_y = abs(points[i][1] - points[i + 1][1])
        if distance_x == distance_y:
            time += distance_y
        elif distance_y > distance_x:
            time += distance_y
        else:
            time += distance_x
    return time

print(minTimeToVisitAllPoints(1,[[3,2],[-2,2]]))

# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/3 17:55
# 文件名：number-of-students-doing-homework-at-a-given-time.py
# 开发工具：PyCharm
def busyStudent(self, startTime, endTime, queryTime) -> int:
    """
    :type startTime: List[int]
    :type endTime: List[int]
    :type queryTime: int
    :rtype: int
    """
    result = 0
    for i in range(len(startTime)):
        if startTime[i] <= queryTime and endTime[i] >= queryTime:
            result += 1
    return result

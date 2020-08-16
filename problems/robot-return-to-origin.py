# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/15 17:33
# 文件名：robot-return-to-origin.py
# 开发工具：PyCharm
def judgeCircle(self, moves):
    """
    :type moves: str
    :rtype: bool
    """
    direction = {"L": [-1, 0], "R": [1, 0], "U": [0, 1], "D": [0, -1]}
    position = [0, 0]
    for i in moves:
        position[0] += direction[i][0]
        position[1] += direction[i][1]
    if position == [0, 0]:
        return True
    else:
        return False


print(judgeCircle(1, "UD"))
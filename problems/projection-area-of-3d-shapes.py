# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/11 9:48
# 文件名：projection-area-of-3d-shapes.py
# 开发工具：PyCharm
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        buttonarea = 0
        leftArea = 0
        rightArea = 0
        for i in range(len(grid)):
            leftArea += max(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    buttonarea += 1
        for j in range(len(grid[0])):
            tmp_max_area = 0
            for i in range(len(grid)):
                if tmp_max_area < grid[i][j]:
                    tmp_max_area = grid[i][j]
            leftArea += tmp_max_area
        return rightArea + leftArea + buttonarea


test = Solution()
print(test.projectionArea([[1,2],[3,4]]))

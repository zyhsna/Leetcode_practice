# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/18 9:11
# 文件名：surface-area-of-3d-shapes.py
# 开发工具：PyCharm
class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: list[list[int]]
        :rtype: int
        """
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    ans += grid[i][j] * 4 + 2
                if i > 0:
                    ans -= min(grid[i + 1][j], grid[i][j]) * 2
                if j > 0:
                    ans -= min((grid[i][j - 1]), grid[i][j]) * 2
        return ans

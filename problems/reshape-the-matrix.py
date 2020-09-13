# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/13 9:47
# 文件名：reshape-the-matrix.py
# 开发工具：PyCharm
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: list[list[int]]
        :type r: int
        :type c: int
        :rtype: list[list[int]]
        """
        if r * c > len(nums) * len(nums[0]):
            return nums

        position = [0, 0]
        ans = [[] for i in range(r)]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if position[1] == c:
                    position[0] += 1
                    position[1] = 0
                if position[0] == r:
                    return ans
                ans[position[0]].append(nums[i][j])
                position[1] += 1
        return ans

test = Solution()
print(test.matrixReshape(nums=
                   [[1, 2], [3, 4]], r=1, c=4)
      )
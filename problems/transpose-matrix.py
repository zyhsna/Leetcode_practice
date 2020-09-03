# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/3 10:57
# 文件名：transpose-matrix.py
# 开发工具：PyCharm
import numpy as np
class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return (np.array(A).T).tolist()
    # 或者 return zip(*A)

test = Solution()
print(test.transpose([[1,2,3],[4,5,6],[7,8,9]]))
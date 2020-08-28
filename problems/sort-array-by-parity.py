# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/28 9:30
# 文件名：sort-array-by-parity.py
# 开发工具：PyCharm
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i, j = 0, len(A) - 1
        while i != j:
            while i != j:
                if A[i] % 2 == 0:
                    i += 1
                else:
                    break
            while j != i:
                if A[j] % 2 != 0:
                    j -= 1
                else:
                    break
            A[i], A[j] = A[j], A[i]
        return A

test = Solution()
print(test.sortArrayByParity([3,1,2,4]))


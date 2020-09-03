# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/3 10:24
# 文件名：sort-array-by-parity-ii.py
# 开发工具：PyCharm
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # i, j = 0, len(A) - 1
        #
        # def oddOrEven(num):
        #     if num % 2 == 0:
        #         return True
        #     return False
        #
        # while i <= j:
        #     count = 0
        #     if oddOrEven(i) and not oddOrEven(A[i]):  # i为偶数但是其中数字不为偶数
        #         count = 0
        #         while i <= j:
        #
        #             if oddOrEven(A[j]) and not oddOrEven(j):
        #                 A[j], A[i] = A[i], A[j]
        #                 break
        #             j -= 1
        #             count += 1
        #     if not oddOrEven(i) and oddOrEven(A[i]):  # i为奇数但是其中数字不为奇数
        #         count = 0
        #         while i <= j:
        #
        #             if not oddOrEven(A[j]) and oddOrEven(j):
        #                 A[j], A[i] = A[i], A[j]
        #                 break
        #             j -= 1
        #             count += 1
        #     j += count
        #     i += 1
        # return A
        # timeout
        ou = [i for i in A if i % 2]
        ji = [i for i in A if not i % 2]
        return [i for n in zip(ji, ou) for i in n]


test = Solution()
print(test.sortArrayByParityII([2, 3, 1, 1, 4, 0, 0, 4, 3, 3]))

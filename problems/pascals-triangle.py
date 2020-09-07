# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/6 17:47
# 文件名：pascals-triangle.py
# 开发工具：PyCharm
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(numRows):
            if i == 0:
                ans.append([1])
            else:
                now_row_ans = []
                aboverow = ans[i - 1]
                for j in range(i + 1):
                    if j == 0 or j == i:
                        now_row_ans.append(1)
                    else:
                        now_row_ans.append(aboverow[j - 1] + aboverow[j])

                ans.append(now_row_ans)
        return ans


test = Solution()
print(test.generate(5))

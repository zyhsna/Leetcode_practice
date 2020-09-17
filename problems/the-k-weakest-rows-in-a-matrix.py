# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/17 12:33
# 文件名：the-k-weakest-rows-in-a-matrix.py
# 开发工具：PyCharm
class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: list[list[int]]
        :type k: int
        :rtype: list[int]
        """
        power_count = []
        rowpeople = len(mat[0])
        for i in range(len(mat)):
            militarycount = 0
            for j in range(rowpeople):
                if mat[i][j] == 0:
                    break
                if mat[i][j] == 1:
                    militarycount += 1
            power_count.append(militarycount)
        count = {}
        for i in range(len(power_count)):
            if power_count[i] not in count.keys():
                count[power_count[i]] = [i]
            else:
                count[power_count[i]].append(i)
        ans = []
        for i in range(len(mat[0])+1):
            if i in count.keys() and k != 0:
                for j in count[i]:
                    k -= 1

                    ans.append(j)
                    if k == 0:
                        break

        return ans


test = Solution()
print(test.kWeakestRows([[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
                        , 1))

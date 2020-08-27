# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/27 10:03
# 文件名：unique-number-of-occurrences.py
# 开发工具：PyCharm
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        times = {}
        for i in arr:
            if i not in times.keys():
                times[i] = 1
            else:
                times[i] += 1
        allCount = []
        for value in times.values():
            allCount.append(value)
        if len(set(allCount)) == len(times):
            return True
        else:
            return False

test = Solution()
print(test.uniqueOccurrences([1,2]))
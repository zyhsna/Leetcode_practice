# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/7 16:38
# 文件名：top-k-frequent-elements.py
# 开发工具：PyCharm
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: list[int]
        :type k: int
        :rtype: List[int]
        """
        nums.sort()
        ans = {}
        count = 0
        for i in nums:
            if i not in ans.keys():
                ans[i] = 1
            else:
                ans[i] += 1
        ans = sorted(ans.items(), key=lambda item: item[1], reverse=True)[:k]
        tmp = []
        for i in ans:
            tmp.append(i[0])
        return tmp


test = Solution()
print(test.topKFrequent([1, 1, 1, 2, 2, 3], 2))

# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/29 9:14
# 文件名：he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof.py
# 开发工具：PyCharm
class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        right, left = 1, 1
        ans = []
        sum = 0
        while left <= target // 2:
            if sum < target:
                sum += right
                right += 1
            elif sum > target:
                sum -= left
                left += 1
            else:
                arr = list(range(left, right))
                ans.append(arr)
                sum -= left
                left += 1
        return ans


test = Solution()
print(test.findContinuousSequence(15))

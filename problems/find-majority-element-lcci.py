# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/17 12:22
# 文件名：find-majority-element-lcci.py
# 开发工具：PyCharm
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for i in nums:
            if i not in count.keys():
                count[i] = 1
            else:
                count[i] += 1
        threshold = len(nums) / 2
        for key, value in count.items():
            if value > threshold:
                return key

        return -1


test = Solution()
print(test.majorityElement([3,2]))

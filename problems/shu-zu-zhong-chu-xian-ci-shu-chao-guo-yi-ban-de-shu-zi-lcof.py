# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/5 10:14
# 文件名：shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof.py
# 开发工具：PyCharm
class Solution(object):
    def majorityElement(self, nums:list):
        """
        :type nums: List
        :rtype: int
        """
        num = set(nums)
        length = len(nums) // 2
        for i in num:
            if nums.count(i) >= length:
                return i


test = Solution()
print(test.majorityElement([1, 2, 3, 2, 2, 2, 5, 4, 2]))
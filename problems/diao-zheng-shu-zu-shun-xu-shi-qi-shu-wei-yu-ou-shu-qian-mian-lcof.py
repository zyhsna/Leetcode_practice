# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/17 16:36
# 文件名：diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof.py
# 开发工具：PyCharm
class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return nums
        i, j = 0, len(nums) - 1
        while i < j and i < len(nums) and j > 0:
            while i < len(nums) and nums[i] % 2 != 0:
                i += 1
            while j > 0 and nums[j] % 2 == 0:
                j -= 1
            if i >= len(nums) or j < 0 or i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]

        return nums

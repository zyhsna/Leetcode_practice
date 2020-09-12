# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/12 14:11
# 文件名：next-greater-element-i.py
# 开发工具：PyCharm
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: list[int]
        :type nums2: list[int]
        :rtype: list[int]
        """
        position = {}
        ans = [_ for _ in range(len(nums1))]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    if j == len(nums2) - 1:
                        ans[i] = -1
                    for k in range(j+1,len(nums2)):
                        if nums2[k] > nums1[i]:
                            ans[i] = nums2[k]
                            break
                        else:
                            ans[i] = -1
        return ans

test = Solution()
print(test.nextGreaterElement([2,4],[1,2,3,4]))
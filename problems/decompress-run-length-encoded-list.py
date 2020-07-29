# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/29 18:56
# 文件名：decompress-run-length-encoded-list.py
# 开发工具：PyCharm
def decompressRLElist(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = []
    for i in range(len(nums) // 2):

        location = 2 * i + 1
        ans.extend([nums[location] for x in range(nums[location - 1])])
    return ans


print(decompressRLElist(1, [1, 2, 3, 4]))

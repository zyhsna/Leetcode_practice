# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/22 10:52
# 文件名：24-game.py
# 开发工具：PyCharm
def judgePoint24(self, nums: list):
    """
    :type nums: List[int]
    :rtype: bool
    """
    ans = []
    if len(nums) > 1:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                y = nums[j]
                nums.remove(j)
                x = nums[i]
                nums.remove(i)
                list.insert(x + y, 0)
                judgePoint24(list, ans)

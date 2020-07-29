# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/7/26 21:05
# 文件名：shuffle-the-array.py
# 开发工具：PyCharm
def shuffle(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: List[int]
    """
    ans = [0 for x in range(len(nums))]
    count = 1
    while count <= n:
        start = (count-1)*2
        ans[start] = nums[count-1]
        ans[start+1] = nums[count-1+n]
        count += 1
    return ans

shuffle([2,5,1,3,4,7], 3)
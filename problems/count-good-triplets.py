# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/7 17:59
# 文件名：count-good-triplets.py
# 开发工具：PyCharm
def countGoodTriplets(self, arr, a, b, c):
    """
    :type arr: List[int]
    :type a: int
    :type b: int
    :type c: int
    :rtype: int
    """
    ans = []
    for i in range(len(arr) - 2):
        for j in range(i + 1, len(arr) - 1):
            for k in range(j + 1, len(arr)):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    ans.append((arr[i], arr[j], arr[k]))
    return len(ans)


print(countGoodTriplets(1, [3, 0, 1, 1, 9, 7], 7, 2, c=3))

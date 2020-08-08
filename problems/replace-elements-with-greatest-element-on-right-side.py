# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/8 17:12
# 文件名：replace-elements-with-greatest-element-on-right-side.py
# 开发工具：PyCharm
def replaceElements(self, arr):
    """
    :type arr: List[int]
    :rtype: List[int]
    """
    for i in range(len(arr)):
        arr[i] = max(arr[i + 1:]) if i < len(arr)-1 else -1
    return arr
print(replaceElements(1,[17,18,5,4,6,1]))
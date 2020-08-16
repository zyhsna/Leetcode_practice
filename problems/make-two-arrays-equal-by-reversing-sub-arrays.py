# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/16 8:55
# 文件名：make-two-arrays-equal-by-reversing-sub-arrays.py
# 开发工具：PyCharm
def canBeEqual(self, target, arr):
    """
    :type target: List[int]
    :type arr: List[int]
    :rtype: bool
    """
    Hash_t, Hash_a = {}, {}
    for i in range(len(target)):
        Hash_t[target[i]] = Hash_t.get(target[i], 0) + 1
        Hash_a[arr[i]] = Hash_a.get(arr[i], 0) + 1
    for key in Hash_t.keys():
        if Hash_a.get(key) is None:
            return False
        else:
            if Hash_a[key] != Hash_t[key]:
                return False
    return True
# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/26 11:12
# 文件名：keyboard-row.py
# 开发工具：PyCharm
# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/26 11:01
# 文件名：comments.py
# 开发工具：PyCharm
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        set1 = set('qwertyuiop')
        set2 = set('asdfghjkl')
        set3 = set('zxcvbnm')
        res = []
        for i in words:
            x = i.lower()
            setx = set(x)
            if setx <= set1 or setx <= set2 or setx <= set3:
                res.append(i)
        return res

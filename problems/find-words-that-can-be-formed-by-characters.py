# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/1 10:47
# 文件名：find-words-that-can-be-formed-by-characters.py
# 开发工具：PyCharm
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        ans = 0
        for w in words:
            for i in w:
                if w.count(i) > chars.count(i):
                    break
            else:
                ans+=len(w)
        return ans
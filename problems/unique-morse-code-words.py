# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/15 11:34
# 文件名：unique-morse-code-words.py
# 开发工具：PyCharm
def uniqueMorseRepresentations(self, words):
    """
    :type words: List[str]
    :rtype: int
    """

    MORSE = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
             "....", "..", ".---", "-.-", ".-..", "--", "-.",
             "---", ".--.", "--.-", ".-.", "...", "-", "..-",
             "...-", ".--", "-..-", "-.--", "--.."]

    seen = {"".join(MORSE[ord(c) - ord('a')] for c in word)
            for word in words}

    return len(seen)
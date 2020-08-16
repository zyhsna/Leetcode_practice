# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/16 8:49
# 文件名：fan-zhuan-lian-biao-lcof.py
# 开发工具：PyCharm
def reverseList(self, head) :
    last = None
    while head:
        # 先赋值head.next,然后last,最后head
        # 其实就是相当于链表倒置
        head.next, last, head = last, head, head.next
    return last
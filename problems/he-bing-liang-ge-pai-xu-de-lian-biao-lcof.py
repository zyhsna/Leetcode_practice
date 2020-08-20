# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/19 10:19
# 文件名：he-bing-liang-ge-pai-xu-de-lian-biao-lcof.py
# 开发工具：PyCharm
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    cur = dum = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            cur.next, l1 = l1, l1.next
        else:
            cur.next, l2 = l2, l2.next
        cur = cur.next
    cur.next = l1 if l1 else l2
    return dum.next

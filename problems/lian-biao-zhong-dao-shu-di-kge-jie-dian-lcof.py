# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/6 17:39
# 文件名：lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof.py
# 开发工具：PyCharm
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def getKthFromEnd(self, head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    tempHead = head
    count = 1
    while tempHead.next != None:
        count += 1
        tempHead = tempHead.next
    count -= k
    while count != 0:
        head = head.next
        count -= 1
    return head

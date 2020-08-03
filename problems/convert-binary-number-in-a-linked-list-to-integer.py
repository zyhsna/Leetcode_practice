# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/3 19:05
# 文件名：convert-binary-number-in-a-linked-list-to-integer.py
# 开发工具：PyCharm
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def getDecimalValue(self, head):
    """
    :type head: ListNode
    :rtype: int
    """
    count = 0
    temp = head
    while head != None:
        count += 1
        head = head.next
    count -= 1
    sum = 0
    head = temp
    while head != None:
        sum += head.val * (2 ** count)
        count -= 1
        head = head.next
    return sum


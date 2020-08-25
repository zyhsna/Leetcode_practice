# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/24 11:44
# 文件名：reverse-linked-list.py
# 开发工具：PyCharm
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp, r_head = head, None

        while tmp:
            r_head, r_head.next, tmp = tmp, r_head, tmp.next
        return r_head

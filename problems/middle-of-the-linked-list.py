# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/28 9:00
# 文件名：middle-of-the-linked-list.py
# 开发工具：PyCharm
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        count = 0
        if not head:
            return head
        tmp = head
        while tmp:
            count += 1
            tmp = tmp.next
        mid = count // 2
        count = 0
        while count != mid:
            head = head.next
            count += 1
        return head
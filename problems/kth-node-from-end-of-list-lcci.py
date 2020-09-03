# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/3 10:14
# 文件名：kth-node-from-end-of-list-lcci.py
# 开发工具：PyCharm
# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        count = 0
        tmp = head
        while tmp:
            count += 1
            tmp = tmp.next
        target = count - k + 1
        count = 1
        while count != target:
            head = head.next
            count += 1
        return head.val

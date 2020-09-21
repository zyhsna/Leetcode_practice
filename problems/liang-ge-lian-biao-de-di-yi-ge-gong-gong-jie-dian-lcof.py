# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/9/18 9:44
# 文件名：liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof.py
# 开发工具：PyCharm
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ListA = []
        ListB = []
        tmpA = headA
# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/25 10:02
# 文件名：remove-duplicate-node-lcci.py
# 开发工具：PyCharm
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeDuplicateNodes(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, next_node = None, head
        num = {}
        while next_node:
            if next_node.val not in num.keys():
                num[next_node.val] = 1
                cur, next_node = next_node, next_node.next
            else:
                cur.next = next_node.next
                next_node = next_node.next.next
            head = head.next
        return head
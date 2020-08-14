# _*_ coding:UTF-8 _*_
# 开发人员：zyh
# 开发时间：2020/8/14 16:47
# 文件名：cong-wei-dao-tou-da-yin-lian-biao-lcof.py
# 开发工具：PyCharm
def reversePrint(self, head):
    """
    :type head: ListNode
    :rtype: List[int]
    """
    ans = []
    while head != None:
        ans.append(head.val)
        head = head.next
    return ans[::-1]
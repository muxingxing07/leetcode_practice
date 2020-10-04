# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = p = ListNode(None) #保存头节点，result返回结果，p用来遍历
        s = 0
        while l1 or l2 or s:  #循环条件：l1或者l2没有遍历完成，s(进位）不为0
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)
            p = p.next
            s //= 10   # 求进位
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return result.next

#一次遍历，dummy节点
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        dummy=ListNode(0)
        dummy.next=head
        pre=dummy
        cur=head
        while cur:
            while cur.next and cur.val==cur.next.val:
                cur=cur.next
            if pre.next==cur:
                pre=pre.next
            else:
                pre.next=cur.next
            cur=cur.next
        return dummy.next
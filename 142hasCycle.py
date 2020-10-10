#解题思路：这类链表题目一般都是使用双指针法解决的，
#例如寻找距离尾部第K个节点、寻找环入口、寻找公共尾部入口等。
#快慢指针，两次相遇
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast, slow = head, head
        while True:
            if not (fast and fast.next):
                return
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast, slow = fast.next, slow.next
        return fast

# 对链表题掌握的不好，应该多练习
#用哈希表，遍历所有节点，判断节点之前是否被访问过
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        result = set()
        while head:
            if head in result:
                return True
            result.add(head)
            head = head.next
        return False

##快慢指针
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow=head
        fast=head.next

        while slow!=fast:
            if not fast or not fast.next:
                return False
            slow=slow.next
            fast=fast.next.next
        return True